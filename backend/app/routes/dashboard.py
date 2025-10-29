# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app import models, schemas
# from app.utils import get_db, get_current_user

# router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

# @router.post("/", response_model=schemas.UserResponse)
# def update_dashboard(
#     data: schemas.UserDashboard,
#     token: str,
#     db: Session = Depends(get_db),
# ):
#     user = get_current_user(token, db)
#     user.description = data.description
#     db.query(models.Link).filter(models.Link.user_id == user.id).delete()
#     for link in data.links[:6]:
#         new_link = models.Link(title=link.title, url=link.url, user_id=user.id)
#         db.add(new_link)
#     db.commit()
#     db.refresh(user)
#     return user

# @router.get("/", response_model=schemas.UserResponse)
# def get_dashboard(token: str, db: Session = Depends(get_db)):
#     user = get_current_user(token, db)
#     return user
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app import models, schemas
from app.utils import get_db, get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.post("/", response_model=schemas.UserResponse)
def update_dashboard(
    data: schemas.UserDashboard,
    authorization: str = Header(...),
    db: Session = Depends(get_db),
):
    # Extract token from "Bearer <token>"
    token = authorization.split(" ")[1]
    user = get_current_user(token, db)

    user.description = data.description
    db.query(models.Link).filter(models.Link.user_id == user.id).delete()

    for link in data.links[:6]:
        new_link = models.Link(title=link.title, url=link.url, user_id=user.id)
        db.add(new_link)

    db.commit()
    db.refresh(user)
    return user


@router.get("/", response_model=schemas.UserResponse)
def get_dashboard(authorization: str = Header(...), db: Session = Depends(get_db)):
    token = authorization.split(" ")[1]
    user = get_current_user(token, db)
    return user
