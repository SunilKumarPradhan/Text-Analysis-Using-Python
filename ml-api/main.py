import json
from pydantic import BaseModel
from fastapi import FastAPI, Request
from imports import analyze_sentiment_nltk
from imports import generate_star_rating_nltk
from imports import generate_star_ratings_for_comments_nltk
from imports import conv

app = FastAPI()



class userModel(BaseModel):
    userId:str
    comments:list

@app.get("/")
def greet():
    return("Sentiment Analysis Model Home")


@app.get("/{user_id}")
def return_analysis(user_id:int,user_obj:userModel):
    analysis_results = generate_star_ratings_for_comments_nltk(user_obj.comments)
    complete_output = {
        "analysis_results": analysis_results
    }
    json_output = json.dumps(complete_output, indent=4)
    print(json_output)
    return(json_output)


