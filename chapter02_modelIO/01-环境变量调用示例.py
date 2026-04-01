from langchain_openai import ChatOpenAI
import os

# 获取对话模型
chat_model = ChatOpenAI(
    model = "gpt-4o-mini",
    base_url = os.environ["OPENAI_BASE_URL"],
    api_key = os.environ["OPENAI_API_KEY"]

)

# 调用模型
response = chat_model.invoke("langchain是什么？")

# 查看响应文本
print(response.content)
