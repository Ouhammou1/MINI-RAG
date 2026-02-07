from fastapi import FastAPI, APIRouter , Depends , UploadFile , File
import os
from helpers.config import get_settings , Settings
from controllers import DataController


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1" , "data"]
)

from fastapi import UploadFile, File

@data_router.post("/upload/{project_id}")
def upload_data(
    project_id: str,
    file: UploadFile = File(...),
):
    is_valid = DataController().validate_upload_file(file)
    return {"valid": is_valid}














