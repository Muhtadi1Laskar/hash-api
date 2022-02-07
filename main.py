from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

@app.get("/")
def index():
	return RedirectResponse("/index.html")

@app.get("/capitalize/")
def capitalize(s: str):
	"""Apply Python's str.upper method to the input `s`."""
	return s.upper()

app.mount("/", StaticFiles(directory="static"), name="static")
