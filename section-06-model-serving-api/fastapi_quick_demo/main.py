from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Hello World!"}

@app.get("/square")
async def root(num: int):
	result = num ** 2
	return {"square": result}


# to start the application run in terminal: uvicorn main:app --reload 
# http://127.0.0.1:8000/square?num=19
# http://127.0.0.1:8000/docs to check automatic documentation
