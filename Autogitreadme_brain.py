import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI as LangchainChatOpenAi
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_perplexity import ChatPerplexity
from langchain_openai import OpenAIEmbeddings

load_dotenv()

############################  For USING OPEN AI #######################################
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
#             model="text-embedding-3-large"   # or "text-embedding-3-large"
#         )
    
#########################  FOR USING GEMINI AS AI   ##############################
# class readme_brain():
#     def __init__(self):
#         self.api_key = os.getenv("GOOGLE_API_KEY")

#     def getLLM(self, max_tokens: int = 1000, temperature: float = 0.3) -> ChatGoogleGenerativeAI:
#         return ChatGoogleGenerativeAI(
#             api_key=self.api_key,
#             model="gemini-1.5-flash",   # or "gemini-1.5-flash" for faster/cheaper
#             temperature=temperature,
#             max_output_tokens=max_tokens
#         )

#     def getEmbeddingsModel(self):
#         return GoogleGenerativeAIEmbeddings(
#             api_key=self.api_key,
#             model="models/embedding-001"
#         )




class readme_brain():
    def __init__(self):
        self.api_key = os.getenv("PPLX_API_KEY") 
        
    def getLLM(self, max_tokens: int = 1000, temperature: float = 0.3):
        # Set OPENAI_API_KEY for Perplexity (it uses OpenAI client internally)
        os.environ["OPENAI_API_KEY"] = self.api_key
        
        return ChatPerplexity(
            temperature=temperature,
            max_tokens=max_tokens,
            model="sonar-pro"
        )

    def getEmbeddingsModel(self):
        
        self.openai_key = os.getenv("OPENAI_API_KEY")
        return OpenAIEmbeddings(
            api_key=self.openai_key,
            model="text-embedding-3-large"
        )
    
#Embeddings are basically for another feature which has not been added