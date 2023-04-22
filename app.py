from fastapi import FastAPI, File, UploadFile, Request
from starlette.responses import FileResponse
from fastapi.templating import Jinja2Templates
import os
import shutil

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    files = os.listdir("uploads/")
    return templates.TemplateResponse("index.html", {"request": request, "files": files})

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

@app.get("/downloadfile/{filename}")
async def download_file(filename: str):
    file_path = f"uploads/{filename}"
    return FileResponse(file_path)

@app.get("/listfiles/")
async def list_files():
    files = os.listdir("uploads/")
    return {"files": files}

@app.get("/sharefile/{filename}/{target_ip}")
async def share_file(filename: str, target_ip: str):
    file_path = f"uploads/{filename}"
    # Code to transfer file to target IP using sockets or another networking library
    return {"message": f"File {filename} has been shared with {target_ip}"}

def create_app():
    os.makedirs("uploads", exist_ok=True)
    return app

if __name__ == '__main__':
    uvicorn.run("app:create_app", host="0.0.0.0", port=8000, reload=True)
