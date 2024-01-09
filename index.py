import requests
import json
import datetime 
import pymongo
from pymongo import MongoClient


client = MongoClient("mongodb+srv://test:test123@cluster0.otzsx8i.mongodb.net/")

db = client.indeed

def insertToDb(jobTitle,jobLink,companyName,companyLocation,jobDescription,Salary,jobMetaData,jobPosting):
    jobs = db.indeed_python_developers
    doc={"jobTitle": jobTitle,
        "jobLink":jobLink,
        "companyName":companyName,
        "companyLocation":companyLocation,
        "jobDescription":jobDescription,
        "salary":Salary,
        "jobMetaData":jobMetaData,
        "jobPosting":jobPosting, 
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
        }
    inserted = jobs.insert_one(doc)
    return inserted.inserted_id


url = "https://api.scrapingdog.com/indeed"
api_key = "659bfff859e84b61df74f93c"
job_search_base_url = "https://in.indeed.com/jobs?q=python+developer&start="
i = 63

while i<94:
    next_page = job_search_base_url+f"{i*10}"
    i += 1
    params = {"api_key": api_key, "url": next_page}
    response = requests.get(url, params=params)
    print("running")
    if response.status_code == 200:
        # Parse the JSON content
        cards = response.json()
        cards.pop()
        for card in cards:
            insertToDb(**card)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
    
    

    
