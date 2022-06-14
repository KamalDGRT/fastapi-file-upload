
# This file will hold a bunch of utility functions

from fastapi import status, HTTPException
from os.path import splitext


def unauthorized(message):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=message
    )


def not_found(message):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message
    )


def invalid_file_type(message):
    raise HTTPException(
        status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        detail=message
    )


def is_valid_image_file(file_name):
    if splitext(file_name)[-1] not in [".jpg", ".jpeg", ".png"]:
        invalid_file_type("Only Image File Types are allowed.")


def error_uploading_file():
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="There was an error uploading the file"
    )


def unprocessable_entity(message):
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=message
    )
