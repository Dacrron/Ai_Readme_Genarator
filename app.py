import os
from Autogitreadme_brain import readme_brain
from helper import Helper
from generators import Generator

class ReadmeGeneratorApp:
    def __init__(self):
        self.brain = readme_brain() 
        self.helper = Helper()
        self.llm = self.brain.getLLM()
        self.embeddings = self.brain.getEmbeddingsModel()
        self.generator = Generator()

    def generate_readme_from_repo_url(self, github_url: str, generation_method:str = "STANDARD README"):
        repo_name = github_url.rsplit('/').split('-1')[-1]

        local_path = self.helper.clone_repo(github_url, repo_name)
        code_text = self.helper.extract_code_from_repo(local_path)
        summary = self.generator.summarize_code(self.llm , code_text)

        if generation_method = "STANDARD README":
            readme_content = self.generator.generate_readme(self.llm, summary)
        else:
            readme_content = self.generator.generate_readme_with_examples_vectorstore(self.llm, self.embeddings, summary)
