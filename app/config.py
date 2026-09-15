import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY,
                timeout=30.0,
                max_retries=2)