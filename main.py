import uvicorn
from fastapi import FastAPI, File, UploadFile
from tempfile import NamedTemporaryFile
import os
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/watch-dog-scan-report")
async def upload():
    data = []
    try:
        with open('/Users/bhargj/worksapce/SG-Hackverse/watchDogFileUploader-server/blockchain_watchdog.csv', 'r') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:
                print('The value of ROW Is : ',rows)
                data.append(rows)
                

    finally:
        print("process done")
    
    return data