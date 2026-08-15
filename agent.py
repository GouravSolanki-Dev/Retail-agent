import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing from .env")

llm = ChatOpenAI(
    model="gpt-5-mini",
    temperature=0
)

response = llm.invoke("Say hello in one short sentence.")

print(response.content)