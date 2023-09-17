from fastapi import FastAPI, Request
from helperfunctions import suggest_lawyer_type


app = FastAPI()



@app.get("/")
def greet():
    return("Chatbot API Home")

@app.get("/{userId}")
def chatbot(userId:int,inputText:str):
    return{suggest_lawyer_type(inputText)}



