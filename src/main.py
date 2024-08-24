from fastapi import FastAPI, File, UploadFile, Form
import os
import uvicorn



app = FastAPI()

UPLOAD_DIRECTORY = "./uploaded_files/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...), new_filename: str = Form(None)):

    if new_filename:
        _, file_extension = os.path.splitext(file.filename)
        filename = new_filename + file_extension
    else:
        filename = file.filename
  
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)

  
  
    for alreadyfile in os.listdir(UPLOAD_DIRECTORY):
      already_file_path = os.path.join(UPLOAD_DIRECTORY, alreadyfile)
      if os.path.isfile(already_file_path):
        os.remove(already_file_path)
  
  
    
    with open(file_path, "wb") as uploadfile:
        uploadfile.write(await file.read())
    
    return {"filename": filename, "file_path": file_path}
  

  
if __name__ == '__main__':
  uvicorn.run(app="main:app", host="0.0.0.0" , port=8000, reload=True)