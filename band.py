from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated
import os,sys
from fastapi.logger import logger
from pydantic import BaseSettings
from fastapi.templating import Jinja2Templates
from main import qanda

class Settings(BaseSettings):
    # ... The rest of our FastAPI settings

    BASE_URL = "http://localhost:8000"
    USE_NGROK = os.environ.get("USE_NGROK", "False") == "True"


settings = Settings()


def init_webhooks(base_url):
    # Update inbound traffic via APIs to use the public-facing ngrok URL
    pass

# Initialize the FastAPI app for a simple web server
app = FastAPI()

templates = Jinja2Templates(directory='templates/')

if settings.USE_NGROK:
    # pyngrok should only ever be installed or initialized in a dev environment when this flag is set
    from pyngrok import ngrok,conf

    # Get the dev server port (defaults to 8000 for Uvicorn, can be overridden with `--port`
    # when starting the server
    #port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 4040
    conf.get_default().auth_token = "<set-token>"
    
    # Open a ngrok tunnel to the dev server
    public_url = ngrok.connect(8000,"http",subdomain="aniket")
    print(public_url)
    logger.info("pgrok tunnel \"{}\" -> \"http://127.0.0.1:{}/docs\"".format(public_url, 9000))

    # Update any base URLs or webhooks to use the public ngrok URL
    settings.BASE_URL = public_url
    init_webhooks(public_url)


class Ques(BaseModel):
    ques: str



@app.get('/form')
def index(request: Request):
    context = {'request': request, 'result': ""}
    return templates.TemplateResponse("index.html", context)

@app.post('/form')
def index(request: Request, question: str = Form(...)):
    result = qanda(question)
    return templates.TemplateResponse("index.html", context = {'request': request, 'result': result})


