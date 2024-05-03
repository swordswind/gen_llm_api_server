import requests


def send_message_to_chatbot(prompt, question):
    # 构建查询参数
    params = {"p": prompt, "q": question}
    url = "http://127.0.0.1:8088/llm/"
    # 发送请求
    response = requests.get(url, params=params)
    # 解析JSON响应
    response_json = response.json()
    # 返回机器人的回答
    return response_json["answer"]


prompt = "你是一个有用的助手"
while True:
    question = input("用户输入问题: ")
    print("消息已发送，等待AI回答...")
    try:
        bot_response = send_message_to_chatbot(prompt, question)
        print(f"千问0.5B(本地)回答: {bot_response}")
    except:
        print("提示: 请先运行大语言模型API服务器，再使用客户端和AI对话。")
