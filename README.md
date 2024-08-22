# FastAPI

## Already made:

1. Postgres Database with all needed structure
2. Authorization - using FastAPI-users lib, JWT token, cookie files. Endpoints are /auth/login or /auth/register
3. Chat working on WebSockets. Also it is private - no one without JWT token cannot access this page and connect via websocket to chat
4. Frontend with Jinja2Templates libray - some simple code so the app can be interacted with

## TO-DO:

1. Profiles
2. Private messaging
3. Authorization via google+, telegram or facebook

## Environmental variables

To get this thing to work you need to setup some variables (look at src/config.py)
