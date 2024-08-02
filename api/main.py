from fastapi import FastAPI 

app = FastAPI(
    docs_url='/', 
    redoc_url='/red',
    title='Real estate API',
    description="A simple api to learn how to build fastapi",
    contact= {
        "name": "Abas Isaac",
        "Gmail": "abasisaac22@gmail.com"
    }         
)

@app.get('/testing')
async def testing_route():
    return {
        "Message": "Testing if the route is working fine or not",
        "data":{"print":"working ... .. ."}
    }