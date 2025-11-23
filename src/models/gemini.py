import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")
gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url
)

gemini_client = OpenAIChatCompletionsModel(
    model=gemini_model,
    openai_client=client
)