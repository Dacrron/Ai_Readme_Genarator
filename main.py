#This is for testing before the front end FAST API implementation 

from app import ReadmeGeneratorApp
import requests

readmeGeneratorApp = ReadmeGeneratorApp()



# Test if the repo exists and is public


def test_repo_access(github_url):
    # Convert GitHub URL to API URL
    if "github.com" in github_url:
        api_url = github_url.replace("github.com", "api.github.com/repos")
        response = requests.get(api_url)
        return response.status_code == 200
    return False

# Test
url = "github url here"
if test_repo_access(url):
    print("Repository is accessible")
    print(readmeGeneratorApp.generate_readme_from_repo_url(url))
else:
    print("Repository might be private or doesn't exist")



