from fastapi import FastAPI, File, UploadFile
from starlette.responses import FileResponse
import os

app = FastAPI()

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

if __name__ == '__main__':
    import shutil
    import uvicorn

    os.makedirs("uploads", exist_ok=True)

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
