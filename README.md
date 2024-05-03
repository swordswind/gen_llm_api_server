# gen_llm_api_server
生成式大语言模型API服务器

## 功能特点
- **快速响应**：基于阿里开发的Qwen1.5-0.5B大语言模型，提供快速、准确的问答服务。
- **上下文记忆**：可选配置，支持对话上下文记忆，使对话更加连贯。
- **API集成**：通过API调用，方便集成到各种应用程序中。
- **JSON格式回答**：服务器返回格式化的JSON数据，易于解析和处理。

## 环境要求
- Python3.x
- fastapi
- transformers
- uvicorn

## 安装依赖
   ```
   pip install -r requirements.txt
   ```

## 使用方法
- **运行服务器**：
  - 无上下文记忆：`python llm_api_server.py`
  - 包含上下文记忆：`python llm_api_server_history.py`
- **访问API**：
  - 使用GET请求，通过浏览器或HTTP客户端访问：
    ```
    http://127.0.0.1:8088/llm/?p=你是一个有用的助手&q=你好
    ```
  - 服务器将返回JSON格式的回答。

## 返回结果示例
当您向API发送请求后，服务器将返回如下格式的JSON数据：
```json
{
  "answer": "你好，有什么我可以帮助你的吗？"
}
```

## 注意事项
- 服务器仅支持GET请求方式。
- 默认端口为8088，如需更改，需修改服务器配置。
- 上下文记忆功能会存储最近的对话记录，以支持更连贯的对话。
- 服务器返回的回答内容仅供参考，如有不准确之处，请以实际问答为准。

## 代码结构
```
llm_api_server/
│
├── llm_api_server.py          # 无上下文记忆的服务器入口
├── llm_api_server_history.py  # 包含上下文记忆的服务器入口
├── requirements.txt           # 项目依赖
└── ...
```

## 贡献与反馈
- 欢迎通过GitHub的Issue和Pull Request功能参与项目的贡献。
- 如有任何疑问或建议，可通过电子邮件或社交媒体与我们联系。

## 开源协议
本项目遵循MIT开源协议。详情参见`LICENSE`文件。
