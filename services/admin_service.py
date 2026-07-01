from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.admin import AdminModel
from schemas.admin import Admin, UpdateAdmin, SearchAdmin


def create_admin_service(admin: Admin, db: Session):

    # Check if admin already exists
    existing_admin = db.query(AdminModel).filter( AdminModel.admin_id == admin.admin_id).first()

    if existing_admin:
        raise HTTPException(status_code=409, detail="Admin already exists")

    # Create SQLAlchemy object
    new_admin = AdminModel(
        admin_id=admin.admin_id,
        first_name=admin.first_name,
        last_name=admin.last_name,
        email=admin.email,
        phone_number=admin.phone_number,
        password_hash=admin.password_hash,
        role=admin.role,
        date_of_joining=admin.date_of_joining,
        is_active=admin.is_active,
        profile_image=admin.profile_image
    )

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    return JSONResponse( status_code=201, content={"message": "Admin created successfully"})


def view_all_admin_service(db: Session):

    admin = db.query(AdminModel).all()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    return admin


def search_admin_service(filters: SearchAdmin, db: Session):

    total_admin = db.query(AdminModel).count()

    # Base Query
    query = db.query(AdminModel)

    # ---------------- Filtering ----------------

    if filters.admin_id:
        query = query.filter(AdminModel.admin_id == filters.admin_id)

    if filters.first_name:
        query = query.filter(AdminModel.first_name.ilike(f"%{filters.first_name}%"))

    if filters.last_name:
        query = query.filter(AdminModel.last_name.ilike(f"%{filters.last_name}%"))

    if filters.email:
        query = query.filter(AdminModel.email == filters.email)

    if filters.phone_number:
        query = query.filter(AdminModel.phone_number == filters.phone_number)

    if filters.role:
        query = query.filter(AdminModel.role == filters.role)

    if filters.date_of_joining:
        query = query.filter(AdminModel.date_of_joining == filters.date_of_joining)

    if filters.is_active is not None:
        query = query.filter(AdminModel.is_active == filters.is_active)

    filtered_admin = query.count()

    # ---------------- Sorting ----------------

    if filters.sort_by:

        column = getattr(AdminModel, filters.sort_by)

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

    admin = query.all()

    return {
        "total_admin": total_admin,
        "filtered_admin": filtered_admin,
        "page": page,
        "limit": limit,
        "admin": admin
    }


def view_particular_admin_service(admin_id: str, db: Session):

    particular_admin = db.query(AdminModel).filter( AdminModel.admin_id == admin_id).first()

    if not particular_admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    return particular_admin


def update_admin_info_service( admin_id: str,update_admin: UpdateAdmin, db: Session):

    existing_admin = db.query(AdminModel).filter(AdminModel.admin_id == admin_id).first()

    if not existing_admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    update_data = update_admin.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(existing_admin, key, value)

    db.commit()
    db.refresh(existing_admin)

    return JSONResponse( status_code=200,content={"message": "Admin updated successfully"} )


def delete_admin_service(admin_id: str, db: Session):

    admin = db.query(AdminModel).filter( AdminModel.admin_id == admin_id).first()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    db.delete(admin)
    db.commit()

    return JSONResponse(status_code=200, content={"message": f"{admin_id} admin deleted successfully"} )