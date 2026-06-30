from sqlalchemy.orm import Session
from models.department import DepartmentModel
from fastapi import HTTPException  
from core.security import hash_password 
from fastapi.responses import JSONResponse
from schemas.departments import UpdateDepartment, SearchDepartment


def create_department_service(department: DepartmentModel, db: Session):

    # Check if department already exists
    existing_department = db.query(DepartmentModel).filter( DepartmentModel.department_id == department.department_id).first()

    if existing_department:
        raise HTTPException(status_code=409,detail="Department already exists")

    # Create SQLAlchemy object
    new_department = DepartmentModel(
        department_id=department.department_id,
        department_name=department.department_name,
        department_code=department.department_code,
        hod_id=department.hod_id,
        hod_name=department.hod_name,
        building=department.building,
        floor=department.floor,
        office_room=department.office_room,
        office_email=department.office_email,
        office_phone=department.office_phone,
        description=department.description,
        established_year=department.established_year,
        is_active=department.is_active)

    # Save to database
    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return JSONResponse(status_code=201,content={"message": "Department created successfully"} )


def view_all_department_service(db:Session):
    
   department = db.query(DepartmentModel).all()

   if not department :
       raise HTTPException(status_code=404, detail="department not found")
   return department

def search_department_service(filters:SearchDepartment, db:Session):

    total_department = db.query(DepartmentModel).count()

    #base query 
    query = db.query(DepartmentModel)

    #--------------filtering------------------

    if filters.department_id:
        query = query.filter(DepartmentModel.department_id == filters.department_id)

    if filters.department_name:
        query = query.filter(DepartmentModel.department_name == filters.department_name) 

    if filters.hod_id:
        query = query.filter(DepartmentModel.hod_teacher_id == filters.hod_teacher_id)

    if filters.hod_name:
        query = query.filter(DepartmentModel.hod_name.ilike(f"%{filters.hod_name}%"))

    if filters.building:
         query = query.filter(DepartmentModel.building== filters.building)

    if filters.floor:
         query = query.filter(DepartmentModel.floor== filters.floor)

    if filters.office_email:
        query = query.filter(DepartmentModel.office_email== filters.office_email)     

    if filters.office_phone:
        query = query.filter(DepartmentModel.office_phone == filters.office_phone)   

    if filters.is_active:
        query = query.filter(DepartmentModel.is_active == filters.is_active)

    if filters.created_at:
        query = query.filter(DepartmentModel.created_at == filters.created_at)        

   #----------------sorting-----------------

    if filters.sort_by:

        column = getattr(DepartmentModel, filters.sort_by)

        if filters.sort_order == "desc":
            query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())


    filtered_department = query.count()      

   #-------------pagination ----------------
    if filters.page is not None and filters.limit is not None:

        page = filters.page
        limit = filters.limit

        offset = (page - 1) * limit

        query = query.offset(offset).limit(limit)

    # Execute query
    department = query.all()

    return {
        "total_department": total_department,
        "filtered_department": filtered_department,
        "page": page,
        "limit": limit,
        "department": department
    }

def view_particular_department_service(department_id : str , db:Session):

    particular_department = db.query(DepartmentModel).filter(DepartmentModel.department_id==department_id).first()

    if not particular_department :
        raise HTTPException (status_code=404, detail="Teacher not found")
    return particular_department
           
def update_department_info_service(department_id : str , update_department: UpdateDepartment ,db:Session ):

    existing_department = db.query(DepartmentModel).filter(DepartmentModel.department_id==department_id).first()

    if not existing_department:
        raise HTTPException(status_code=404, detail="Department not found")
    
    update_data = update_department.model_dump(exclude_unset=True)

    for key,value in update_data.items():
        setattr(existing_department, key , value)

    db.commit()
    db.refresh(existing_department)

    return JSONResponse(status_code=200, content={'message':'Department updated successfully'})  


def delete_department_service(department_id:str, db:Session):
    department = db.query(DepartmentModel).filter(DepartmentModel.department_id==department_id).first()

    if not department:
        raise HTTPException (status_code=404, detail="Department not found")
    
    db.delete(department)
    db.commit()

    return JSONResponse(status_code=200, content={'message':f" {department_id} department deleted"})












