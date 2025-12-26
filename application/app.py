from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

app.mount("/cv-simple", StaticFiles(directory="pages/cv-simple", html=True), name="cv-simple")

@app.get("/")
async def redirect_to_cv():
    return RedirectResponse(url="/cv-simple/index.html")
