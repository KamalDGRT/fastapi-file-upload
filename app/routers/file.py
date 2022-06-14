from http.client import HTTPException
from os import rename
from os.path import exists
import uuid

from sqlalchemy.orm import Session
from fastapi import status, APIRouter, UploadFile, File, Depends

from app.utils import  error_uploading_file, is_valid_image_file
from app.database import get_db

router = APIRouter(
    prefix='/file',
    tags=['File Upload']
)


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_a_file(file: UploadFile = File(...),  db: Session = Depends(get_db)):
    try:
        is_valid_image_file(file.filename)
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

    except HTTPException:
        pass
