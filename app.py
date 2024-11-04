from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from starlette.responses import FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os
import shutil
import socket
import uvicorn

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
    return RedirectResponse(url="/", status_code=303)

@app.get("/downloadfile/{filename}")
async def download_file(filename: str):
    file_path = f"uploads/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.post("/deletefile/{filename}")
async def delete_file(filename: str):
    file_path = f"uploads/{filename}"
    if os.path.exists(file_path):
        os.remove(file_path)
        return RedirectResponse(url="/", status_code=303)
    else:
        raise HTTPException(status_code=404, detail="File not found")

def get_local_ip():
    # This function retrieves the local IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable
        s.connect(('10.254.254.254', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

def create_app():
    os.makedirs("uploads", exist_ok=True)
    local_ip = get_local_ip()
    print(f"Server is running on http://{local_ip}:8000")
    return app

if __name__ == '__main__':
    uvicorn.run("app:create_app", host="0.0.0.0", port=8000, reload=True)
