from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configure CORS settings to allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Add OPTIONS method here
    allow_headers=["*"],
)

# Define your model
class InputData(BaseModel):
    api_key: str
    param1: float
    param2: float
    param3: float

# Define your prediction endpoint
@app.post("/predict/")
async def predict(data: InputData):
    # Validate the API key
    if data.api_key != "your_api_key":
        raise HTTPException(status_code=401, detail="Invalid API key")

    # Your prediction logic goes here
    output1 = data.param1 * 2
    output2 = data.param2 + data.param3
    return {"output1": output1, "output2": output2}
