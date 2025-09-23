from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate 
import os

class Generator:

    def summarize_code(self, llm, code_text):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 3000,
            chunk_overlap = 200,
            separators = ["\nFile:", "\n\n", "\n", " ","" ]
        )

        chunks = text_splitter.split_text(code_text)
        documents = [Document(page_content=chunk)for chunk in chunks]
        print(f"Split code into {len(documents) } chunks for processing ")
        chain = load_summarize_chain(llm, chain_type = "map_reduce")
        return chain.invoke({"input_documents": documents})
    
    # def generate_readme_with_examples_vectorstore(self, llm, embeddings, summary : str) -> str:
    #     if not isinstance(summary, str):
    #         summary = str(summary)

    #     example_docs = []
    #     for root, dirs, files in os.walk("examples"):
    #         for file in files:
    #             if file.endswith(('.md')):
    #                 file_path = os.path.join(root, file)
    #                 try:
    #                     with open(file_path, 'r', encoding='utf-8') as f:
    #                         content = f.read()
    #                         example_docs.append(Document(
    #                             page_content= content,
    #                             metadata = {"Source" : file_path, "type" : "example" }
    #                         ))
    #                 except Exception as e:
    #                     print(f"Failed to read the file -> {file}: {e}")

    #     if not example_docs:
    #         return self.generate_readme(llm, summary)








    def generate_readme(self, llm, summary):
        if not isinstance(summary, str):
            summary =str(summary)

        docs = [Document(page_content=summary)]
        map_template = """
            Analyze this portion of a codebase  summary and extract the most important information:

            {text}

            KEYPOINTS: 
        """

        map_prompt = PromptTemplate(template= map_template,  input_variables = ["text"] )
        
        combine_template = """
        Based on these key points from a codebase analysis, create a consise summary that captures the essence of the project:

        {text}

        CONSISE SUMMARY : 
        """

        combine_prompt = PromptTemplate(template=combine_template, input_variables=["text"])

        if(len(summary) > 2000):
            print(f"Summary is large {len(summary) } Considering first...")

            text_spliter = RecursiveCharacterTextSplitter(
                chunk_size = 1000,
                chunk_overlap = 100,
                separators = ["\n\n", "\n", ". ", " ", ""]

            )

            split_docs = text_spliter.split_documents(docs)
            print(f"Split summary into {len(split_docs)} chunks")

            chain = load_summarize_chain(llm, chain_type= "map_reduce", map_prompt = map_prompt, combine_prompt = combine_prompt, verbose = True )
            condensed_result = chain.invoke({"input_documents": split_docs})
            condensed_summary = condensed_result if isinstance(condensed_result, str) else condensed_result.get('output_text', '')
            print(f"Condensed the summary from {len(summary)} to {len(condensed_summary)}")

        else:
            condensed_summary = summary
        
        
        prompt= f"""
        You are a professional technical writer. Based on the following codebase summary, generate a complete README.md file. 

        Include:
        - Project Title: Clear and descriptive
        - Description: Overview of what the project does and its purpose
        - Architecture: How the components work together (if applicable)
        - Prerequisites: Required software, accounts, and configurations
        - Installation: Step-by-step setup instructions
        - Configuration: Environment variables, settings, and Azure-specific configurations
        - Usage: How to use the software with examples
        - API Reference: If the project exposes APIs (if applicable)
        - Development: Instructions for contributors (if applicable)
        - Deployment: How to deploy to Azure (if applicable)
        - Security: Security considerations and best practices
        - Troubleshooting: Common issues and solutions
        - License: Project license information

        Summary:
        {condensed_summary}
        """
        try:
            return llm.invoke(prompt)
        except Exception as e:
            print(f"Error caught -> {e}")