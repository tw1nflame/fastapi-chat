from fastapi import APIRouter, Depends, HTTPException, Query, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
import json
import jwt
from auth.models import User
from chat.connection import ConnectionManager
from auth.base_config import fastapi_users, get_jwt_strategy
from auth.manager import UserManager, get_user_manager
from auth.base_config import fastapi_users
from fastapi_users.authentication import JWTStrategy

router = APIRouter(
    prefix="",
    tags=["chat"]
)

templates = Jinja2Templates(directory="../templates")

current_user = fastapi_users.current_user(optional=True)


@router.get("/")
def get_chat_page(request: Request, user: User = Depends(current_user)):
    if user:
        return templates.TemplateResponse("chat.html", {"request": request, "user": user})
    else:
        return templates.TemplateResponse("no-logged.html", {"request": request})


manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str = Query(...), user_manager: UserManager = Depends(get_user_manager), jwt_strategy: JWTStrategy = Depends(get_jwt_strategy)):

    user = await jwt_strategy.read_token(token, user_manager)
    print(user.first_name)

    if not user:
        await websocket.close(code=4000)  # close with an error code
        return

    data = {
        "type": 'info',
        'info': f"Пользователь {user.first_name} {user.last_name} присоединился к чату"
    }

    await manager.broadcast(json.dumps(data))
    await manager.connect(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            data = {
                "message": message,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "type": "message"
            }
            await manager.broadcast(json.dumps(data))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        data = {
            "type": 'info',
            'info': f"Пользователь {user.first_name} {user.last_name} покинул чат"
        }

        await manager.broadcast(json.dumps(data))
    except Exception as e:
        print(e)
        await websocket.close()
