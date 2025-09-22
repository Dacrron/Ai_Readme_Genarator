import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI as LangchainChatOpenAi
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

load_dotenv()


# class readme_brain():
#     def __init__(self):
#         self.api_key = os.getenv("OPEN_API_KEY") 


#     def getLLM(self, max_tokens: int = 1000, temperature: float = 0.3 ) -> LangchainChatOpenAi:
#         return LangchainChatOpenAi(
#             api_key= self.api_key,
#             temperature = temperature,
#             max_tokens = max_tokens,
#             model   ="gpt-4o-mini"
#         )

#     def getEmbeddingsModel(self):
#         return OpenAIEmbeddings(
#             api_key=self.api_key,
#             model="gpt-4o-mini"   # or "text-embedding-3-large"
#         )
    
#FOR USING GEMINI AS AI
class readme_brain():
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")

    def getLLM(self, max_tokens: int = 1000, temperature: float = 0.3) -> ChatGoogleGenerativeAI:
        return ChatGoogleGenerativeAI(
            api_key=self.api_key,
            model="gemini-1.5-flash",   # or "gemini-1.5-flash" for faster/cheaper
            temperature=temperature,
            max_output_tokens=max_tokens
        )

    def getEmbeddingsModel(self):
        return GoogleGenerativeAIEmbeddings(
            api_key=self.api_key,
            model="models/embedding-001"
        )