import os

from fastapi import APIRouter, HTTPException

from app.services.indexing_service import index_codebase

router = APIRouter()


@router.post("/documents/index")
async def index_directory(directory: str = "./data"):
    if not os.path.exists(directory):
        raise HTTPException(status_code=404, detail=f"Directory not found: {directory}")
    count = index_codebase(directory)
    return {"indexed_chunks": count, "directory": directory}
