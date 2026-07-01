from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database.session import get_db
from schemas.fees import Fees, SearchFees, UpdateFees, FeesResponse
from services.fees_service import  create_fees_service, search_fees_service, view_all_fees_service, view_particular_fee_service, update_fee_info_service, delete_fee_service


router = APIRouter(prefix="/fees", tags=["Fees"])


@router.post("/create")
def create_fee(fees: Fees, db: Session = Depends(get_db)):
    return create_fees_service(fees, db)


@router.get("/", response_model=List[FeesResponse])
def view_all_fees(db: Session = Depends(get_db)):
    return view_all_fees_service(db)


@router.get("/search")
def search_fees(filters: SearchFees = Depends(), db: Session = Depends(get_db)):
    return search_fees_service(filters, db)


@router.get("/{fee_id}", response_model=FeesResponse)
def view_particular_fee(fee_id: str, db: Session = Depends(get_db)):
    return view_particular_fee_service(fee_id, db)


@router.put("/{fee_id}")
def update_fee_info(fee_id: str,update_fee: UpdateFees, db: Session = Depends(get_db)):
    return update_fee_info_service(fee_id, update_fee, db)


@router.delete("/{fee_id}")
def delete_fee(fee_id: str, db: Session = Depends(get_db)):
    return delete_fee_service(fee_id, db)