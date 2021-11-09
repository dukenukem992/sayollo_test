# Test application for Sayollo

## Task definition
Create application with 3 endpoints(GetAd, Impression, GetStat)

### Endpoints
- http://0.0.0.0:5000/stat/GetStats?filter_type=USER (GET)
- http://0.0.0.0:5000/stat/Impression (POST)
- http://0.0.0.0:5000/stat/GetAd (POST)
For more details about endpoint after deploying go to:
- http://0.0.0.0:5000/docs/
for swagger view

### Responce body 
````
{
    "username":"dukenukem",
    "sdk":"v1",
    "platform":".net",
    "session_id":"0007",
    "country_code":"BY"
}
````
## How to run
- rename .env_example into .env
- push command ``
- docker-compose up -d``

## Requirements.txt
````
fastapi==0.70.0
uvicorn==0.11.3
pydantic==1.8.2
SQLAlchemy==1.4.26
requests==2.26.0
psycopg2-binary==2.9.1
````
## Why I use this technologies
FastAPI is one of the fastest web frameworks (according to tests from https://www.techempower.com/benchmarks/), 
capable of providing "asynchronous out of the box" and fast deployments. 
It is a good solution for both microservices and serverless architecture. 
Having swagger "out of the box" makes writing documentation and understanding how the API works more readable. 
The presence of SQLALchemy allows you to write more flexible queries when using python style.