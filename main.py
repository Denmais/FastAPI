from fastapi import FastAPI
from utilsx.message import func
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    text: str


@app.post("/files")
def create_file(message: Message):
    print(123)

    return {"Newmessage": func(message.text)}
