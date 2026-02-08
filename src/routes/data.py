from fastapi import FastAPI, APIRouter , Depends , UploadFile , File , status
from  fastapi.responses import JSONResponse
import os
from helpers.config import get_settings , Settings
from controllers import DataController , ProjectController
import aiofiles
from models import ResponseSignal


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1" , "data"]
)


@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile = File(...),
):
    is_valid  , result_signal = DataController().validate_upload_file(file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=
                {
                    "result signal": result_signal,
                    "valid": is_valid
                })

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    
    file_path = os.path.join(project_dir_path,file.filename)
    
    async with aiofiles.open(file_path ,"wb") as f:
        while chunk := await file.read(app_setting.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chunk)

    # print(f"file_path = {file_path}\n\n")
    return JSONResponse(
        content=
            {
                "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            })













