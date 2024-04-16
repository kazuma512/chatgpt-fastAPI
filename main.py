from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=''
)

app = FastAPI()

# Configure CORS settings to allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify specific origins instead of "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    input: str

@app.post("/chat")
async def chat(data: ChatInput):
    chat_input = data.input
    response = await ask_gpt(chat_input)
    print(response)
    return {"response": response}

async def ask_gpt(input_text):
    completion = await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": input_text}])
    return completion.choices[0].message.content
