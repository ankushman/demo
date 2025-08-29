from fastapi import FastAPI,HTTPException,Form
from twilio.rest import Client 
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
twilio_number = os.getenv("twilio_number")

import uvicorn
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from the API!"}


client = Client(account_sid, auth_token)

@app.post("/sms")
async def sms_reply(From: str = Form(...), Body: str = Form(...)):
    query = Body.lower()

    # Simple chatbot logic
    if "fever" in query or "bukhar" in query:
        reply = "Drink plenty of water and take paracetamol if needed. Consult a doctor if fever persists."
    elif "cough" in query or "khansi" in query:
        reply = "For cough, drink warm water and honey. Visit health center if severe."
    else:
        reply = "Sorry, I didn’t understand. Can you ask in simple terms?"

    # Send SMS back
    client.messages.create(
        body=reply,
        from_=twilio_number,
        to=From
    )

    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)  

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)