import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI as LangchainChatOpenAi
from langchain_openai import OpenAIEmbeddings

load_dotenv()


class readme_brain():
    def __init__(self):
        self.api_key = os.getenv("OPEN_API_KEY") 


    def getLLM(self, max_tokens: int = 1000, temperature: float = 0.3 ) -> LangchainChatOpenAi:
        return LangchainChatOpenAi(
            api_key= self.api_key,
            temperature = temperature,
            max_tokens = max_tokens,
            model   ="gpt-4o-mini"
        )

    def getEmbeddingsModel(self):
        return OpenAIEmbeddings(
            api_key=self.api_key,
            model="text-embedding-3-small"   # or "text-embedding-3-large"
        )