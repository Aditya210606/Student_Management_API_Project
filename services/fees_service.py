from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.fees import FeesModel
from schemas.fees import Fees, UpdateFees, SearchFees


def create_fees_service(fees: Fees, db: Session):

    # Check if fee record already exists
    existing_fee = db.query(FeesModel).filter( FeesModel.fee_id == fees.fee_id ).first()

    if existing_fee:
        raise HTTPException(status_code=409, detail="Fee record already exists")

    # Create SQLAlchemy object
    new_fee = FeesModel(
        fee_id=fees.fee_id,
        student_id=fees.student_id,
        academic_year=fees.academic_year,
        semester=fees.semester,
        tuition_fee=fees.tuition_fee,
        library_fee=fees.library_fee,
        exam_fee=fees.exam_fee,
        hostel_fee=fees.hostel_fee,
        transport_fee=fees.transport_fee,
        other_fee=fees.other_fee,
        total_fee=fees.total_fee,
        paid_amount=fees.paid_amount,
        pending_amount=fees.pending_amount,
        payment_status=fees.payment_status,
        payment_method=fees.payment_method,
        payment_date=fees.payment_date,
        transaction_id=fees.transaction_id,
        remarks=fees.remarks
    )

    db.add(new_fee)
    db.commit()
    db.refresh(new_fee)

    return JSONResponse( status_code=201, content={"message": "Fee record created successfully"} )


def view_all_fees_service(db: Session):

    fees = db.query(FeesModel).all()

    if not fees:
        raise HTTPException(status_code=404, detail="Fee records not found")

    return fees


def search_fees_service(filters: SearchFees, db: Session):

    total_fees = db.query(FeesModel).count()

    # Base Query
    query = db.query(FeesModel)

    # ---------------- Filtering ----------------

    if filters.fee_id:
        query = query.filter(FeesModel.fee_id == filters.fee_id)

    if filters.student_id:
        query = query.filter(FeesModel.student_id == filters.student_id)

    if filters.academic_year:
        query = query.filter(FeesModel.academic_year == filters.academic_year)

    if filters.semester is not None:
        query = query.filter(FeesModel.semester == filters.semester)

    if filters.tuition_fee is not None:
        query = query.filter(FeesModel.tuition_fee == filters.tuition_fee)

    if filters.library_fee is not None:
        query = query.filter(FeesModel.library_fee == filters.library_fee)

    if filters.exam_fee is not None:
        query = query.filter(FeesModel.exam_fee == filters.exam_fee)

    if filters.hostel_fee is not None:
        query = query.filter(FeesModel.hostel_fee == filters.hostel_fee)

    if filters.transport_fee is not None:
        query = query.filter(FeesModel.transport_fee == filters.transport_fee)

    if filters.other_fee is not None:
        query = query.filter(FeesModel.other_fee == filters.other_fee)

    if filters.total_fee is not None:
        query = query.filter(FeesModel.total_fee == filters.total_fee)

    if filters.paid_amount is not None:
        query = query.filter(FeesModel.paid_amount == filters.paid_amount)

    if filters.pending_amount is not None:
        query = query.filter(FeesModel.pending_amount == filters.pending_amount)

    if filters.payment_status:
        query = query.filter(FeesModel.payment_status == filters.payment_status)

    if filters.payment_method:
        query = query.filter(FeesModel.payment_method == filters.payment_method)

    if filters.payment_date:
        query = query.filter(FeesModel.payment_date == filters.payment_date)

    if filters.transaction_id:
        query = query.filter(FeesModel.transaction_id == filters.transaction_id)

    filtered_fees = query.count()

    # ---------------- Sorting ----------------

    if filters.sort_by:

        column = getattr(FeesModel, filters.sort_by)

        if filters.sort_order == "desc":
            query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())

    # ---------------- Pagination ----------------

    if filters.page is not None and filters.limit is not None:

        page = filters.page
        limit = filters.limit

        offset = (page - 1) * limit

        query = query.offset(offset).limit(limit)

    fees = query.all()

    return {
        "total_fees": total_fees,
        "filtered_fees": filtered_fees,
        "page": page,
        "limit": limit,
        "fees": fees
    }


def view_particular_fee_service(fee_id: str, db: Session):

    particular_fee = db.query(FeesModel).filter( FeesModel.fee_id == fee_id ).first()

    print("Step 2")

    print(particular_fee)

    print("Step 3")

    print(particular_fee.student_id)

    print("Step 4")

    print(particular_fee.students)

    print("Step 5")

    print(particular_fee.students.first_name)

    if not particular_fee:
        raise HTTPException(status_code=404, detail="Fee record not found")

    return particular_fee


def update_fee_info_service( fee_id: str, update_fee: UpdateFees, db: Session):

    existing_fee = db.query(FeesModel).filter( FeesModel.fee_id == fee_id).first()

    if not existing_fee:
        raise HTTPException(status_code=404, detail="Fee record not found")

    update_data = update_fee.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(existing_fee, key, value)

    db.commit()
    db.refresh(existing_fee)

    return JSONResponse(status_code=200, content={"message": "Fee record updated successfully"})


def delete_fee_service(fee_id: str, db: Session):

    fee = db.query(FeesModel).filter(FeesModel.fee_id == fee_id ).first()

    if not fee:
        raise HTTPException(status_code=404, detail="Fee record not found")

    db.delete(fee)
    db.commit()

    return JSONResponse( status_code=200, content={"message": f"{fee_id} fee record deleted successfully"})