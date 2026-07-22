from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database.session import get_db
from schemas.admin import Admin, SearchAdmin, UpdateAdmin, AdminResponse
from services.admin_service import create_admin_service, search_admin_service, view_all_admin_service, view_particular_admin_service, update_admin_info_service, delete_admin_service


router = APIRouter(prefix="/admin", tags=["Admin"])


@router.post("/create")
def create_admin(admin: Admin, db: Session = Depends(get_db)):
    return create_admin_service(admin, db)


@router.get("/", response_model=List[AdminResponse])
def view_all_admin(db: Session = Depends(get_db)):
    return view_all_admin_service(db)


@router.get("/search")
def search_admin(filters: SearchAdmin = Depends(), db: Session = Depends(get_db)):
    return search_admin_service(filters, db)


@router.get("/{admin_id}", response_model=AdminResponse)
def view_particular_admin(admin_id: str, db: Session = Depends(get_db)):
    return view_particular_admin_service(admin_id, db)


@router.put("/{admin_id}")
def update_admin_info( admin_id: str, update_admin: UpdateAdmin, db: Session = Depends(get_db)):
    return update_admin_info_service(admin_id, update_admin, db)


@router.delete("/{admin_id}")
def delete_admin( admin_id: str, db: Session = Depends(get_db)):
    return delete_admin_service(admin_id, db)