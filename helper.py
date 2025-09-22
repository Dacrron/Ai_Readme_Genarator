from git import Repo

import os

class Helper:

    def clone_repo(self, github_url: str, folderName: str = "cloned_repo" ) -> str:
        if os.path.exists(folderName):
            print(f"This {folderName} already exists")
        else:
            Repo.clone_from(github_url, folderName)
            print(f"Cloned in {folderName} folder")
        return folderName
            
    def extract_code_from_repo(self, folderName: str) -> str:
        code_text = ""

        for root, dir, files in os.walk(folderName):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    text_extension = {'.py','.md','.txt','.json','.yaml','.csv','.ini','.cfg','.xml','.html','.js','.css','.java','.c','.cpp','.ts','.go','.rs','.rb','.php','.sh','.bat'}
                    _ , ext = os.path.splitext(file)
                    if ext.lower() not in text_extension:
                        continue
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        code_text += f"File:{file_path}\n{content}\n\n"        
                         
                except Exception as e:
                    print(f"Exception in reading {file} : {e}")
        return code_text


