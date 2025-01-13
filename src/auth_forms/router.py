from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from template import templates

router = APIRouter(
    prefix="/auth",
    tags=["login"]
)


@router.get("/login")
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/register")
def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})
