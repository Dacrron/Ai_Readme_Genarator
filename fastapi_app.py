from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel
import os 
from app import ReadmeGeneratorApp


app = FastAPI(
    title = "Ai Readme Generator",
    description = "Open Ai or Gemini backend Readme Generator",
    version = "2.0.0"
)

try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
except RuntimeError as e:
    print(f"Error occured while mounting the files-> {e}")

templates = Jinja2Templates(directory="templates")

class ReadmeRequest(BaseModel):
    repo_url: str
    generation_method: str = "Standard README"

class ReadmeResponse(BaseModel):
    success : bool
    readme_content : str = ""
    error_message : str = ""
    repo_url : str
    generation_method : str

readmeapp = ReadmeGeneratorApp()

@app.get("/", response_class=HTMLResponse)
async def home_page(request : Request):
    return templates.TemplateResponse(
        "home_page.html",{
            "request": request
        }
    )

@app.post("/api/generate-readme", response_model= ReadmeResponse)
async def generate_readme(request : ReadmeRequest, http_request : Request):


       ##################################   Use this fOR tEST    ########################################################### 
    #  return ReadmeResponse(
    #     success=True,
    #     readme_content="",
    #     error_message="",
    #     repo_url=request.repo_url,
    #     generation_method=request.generation_method
    # )

     if not request.repo_url.startswith(('https://github.com/', 'http://github.com/')):
         return ReadmeResponse(
             success=False,
             error_message="Please provide a valid GitHub repository URL",
             repo_url=request.repo_url,
             generation_method=request.generation_method
         )
     try:
         
         print(f"Generating README for: {request.repo_url}")
         readme_response = readmeapp.generate_readme_from_repo_url(request.repo_url, request.generation_method)
       
         # Extract the string content from AIMessage object FIRST
         if hasattr(readme_response, 'content'):
             readme_content = readme_response.content
         elif isinstance(readme_response, str):
             readme_content = readme_response
         else:
             # Convert to string if it's some other type
             readme_content = str(readme_response)
       
         return ReadmeResponse(
             success=True,
             readme_content=readme_content,  
             repo_url=request.repo_url,
             generation_method=request.generation_method
         )
       
     except Exception as e:
         return ReadmeResponse(
             success=False,
             error_message=f"An error occurred while generating the README: {str(e)}",
             repo_url=request.repo_url,
             generation_method=request.generation_method
       )