# gen_llm_api_server
Generative Large Language Model API Server

## Features
- **Fast Response**: Based on the Qwen1.5-0.5B large language model developed by Alibaba, providing fast and accurate Q&A services.
- **Context Memory**: Optional configuration, supports dialogue context memory, making the conversation more coherent.
- **API Integration**: Convenient integration into various applications through API calls.
- **JSON Format Response**: The server returns formatted JSON data, which is easy to parse and process.

## Environment Requirements
- Python3.x
- fastapi
- transformers
- uvicorn

## Installation of Dependencies
   ```
   pip install -r requirements.txt
   ```

## Usage
- **Run the Server**:
  - Without context memory: `python llm_api_server.py`
  - With context memory: `python llm_api_server_history.py`
- **Access the API**:
  - Use a GET request, access via a browser or HTTP client:
    ```
    http://127.0.0.1:8088/llm/?p=你是一个有用的助手&q=你好
    ```
  - The server will return a JSON formatted response.

## Example of Return Results
After you send a request to the API, the server will return the following format of JSON data:
```json
{
  "answer": "Hello, how can I assist you?"
}
```

## Notes
- The server only supports the GET request method.
- The default port is 8088, if you need to change it, you need to modify the server configuration.
- The context memory feature will store the most recent dialogue records to support more coherent conversations.
- The content of the server's response is for reference only, if there are any inaccuracies, please refer to the actual Q&A.

## Code Structure
```
llm_api_server/
│
├── llm_api_server.py          # Server entry without context memory
├── llm_api_server_history.py  # Server entry with context memory
├── requirements.txt           # Project dependencies
└── ...
```

## Contribution and Feedback
- Contributions to the project are welcome through GitHub's Issue and Pull Request features.
- For any questions or suggestions, you can contact us via email or social media.

## Open Source License
This project follows the MIT open source license. For details, see the `LICENSE` file.
