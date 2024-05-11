from fastapi import FastAPI, Depends, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from connections.database import get_db
from connections.models import WebWaitList
from sqlmodel import Session,select
from pydantic import BaseModel, EmailStr, ValidationError

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]


app = FastAPI(
    title="EON Power waitlist API",
    middleware=middleware,
    debug=True,
    description="Rest API endpoints for the EON wailist backend",
    version="1.0.0",
    terms_of_service="",
)



class Waitlist(BaseModel):
    email: EmailStr
    name: str | None




@app.get("/")
def health_check():
    return {"message":"All the way up!"}
    


@app.post("/waitlist")
async def submit_waitlist(
    body: Waitlist, response: Response, db: Session = Depends(get_db)
):
    try:
        
        statement = (
            select(WebWaitList)
            .filter(WebWaitList.email == body.email.lower())
        )
        check = db.exec(statement).one()

        if check:
            response.status_code = 200
            return {"success": True, "message": "submitted successfully"}
        
        db.add(WebWaitList(name=body.name, email=body.email.lower()))
        db.commit()

        response.status_code = 200
        return {"success": True, "message": "submitted successfully"}
    
    except ValidationError as a:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {"success": False, "message": a.with_traceback()}
    
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(e.args)
        return {"success": False, "message": "Internal Server Error"}
