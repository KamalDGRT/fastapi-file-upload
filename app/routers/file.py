from os import rename
from os.path import exists
import uuid

from fastapi import status, APIRouter, UploadFile, File
from app.utils import  error_uploading_file

router = APIRouter(
    prefix='/file',
    tags=['File Upload']
)


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_a_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open(f'storage/{file.filename}', 'wb') as new_file:
            new_file.write(contents)
        new_file_name = "_".join([str(uuid.uuid4()), file.filename])        
        if exists(f'storage/{file.filename}'):    
            rename(f'storage/{file.filename}', f'storage/{new_file_name}')
        await file.close()

        return {"filename": new_file_name}
    except Exception:
        error_uploading_file()
