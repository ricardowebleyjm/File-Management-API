from fastapi import APIRouter, UploadFile, File, Depends
from app.api.supabase import get_supabase
router = APIRouter(
    prefix="/api/v1/files",
    tags=["Files"]
)

@router.post("")
async def upload_file(file: UploadFile = File(...), supabase = Depends(get_supabase)):
    """Post a file to the endpoint to be uploaded"""
    
    file_content = await file.read()
    result: dict = {
        "message": "success",
    }
    
    return result