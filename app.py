from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/sms")
async def sms_reply(From: str = Form(...), Body: str = Form(...)):
    print(f"Message from {From}: {Body}")
    return PlainTextResponse("Message received")




@app.get("/")
async def root():
    return {"message": "Hello from test API!"}

import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)

    
