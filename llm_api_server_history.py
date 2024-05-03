from fastapi import FastAPI, Query
import uvicorn
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

app = FastAPI()
# 指定设备
device = "cpu"
# 加载模型和分词器
model_name = "Qwen1.5-0.5B-Chat"
model = None
tokenizer = None
context_history = []
context_max_length = 10


def chat_with_model(prompt, question):  # 使用预训练模型进行对话
    global model, tokenizer, streamer
    if not model and not tokenizer:
        model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        streamer = TextStreamer(tokenizer)  # 创建TextStreamer实例
    messages = [{"role": "system", "content": prompt}, {"role": "user", "content": question}]
    # 使用tokenizer处理对话历史，生成模型输入
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to(device)  # 将输入数据放到CPU上
    # 生成回答
    generated_ids = model.generate(model_inputs.input_ids, max_new_tokens=2048, pad_token_id=tokenizer.eos_token_id,
                                   streamer=streamer)
    # 将生成的token ids转换为文本
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response


def ask_llm(prompt, question):
    context_history.append(question)
    if len(context_history) > context_max_length:
        context_history.pop(0)
    question = " ".join(context_history)
    response = chat_with_model(prompt, question)
    index = response.rfind("assistant")
    if index != -1:
        res = response[index + len("assistant"):]
    else:
        res = "抱歉，我不明白您的意思，换个话题吧。"
    context_history.append(response)  # 添加机器人的回答到历史记录中
    if len(context_history) > context_max_length:
        context_history.pop(0)
    return res


@app.get("/llm/")  # 使用举例：http://127.0.0.1:8088/llm/?p=你是一个有用的助手。&q=你好
async def get_result(p: str = Query(...), q: str = Query(...)):
    answer = ask_llm(p, q)
    return {"answer": answer}

print("\n本地大语言模型API服务器(上下文记忆版)启动成功!\n")
uvicorn.run(app, host="0.0.0.0", port=8088)
