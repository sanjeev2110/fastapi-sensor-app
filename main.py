from fastapi import FastAPI
from pydantic import BaseModel
from random import uniform

# Initialize the FastAPI app
app = FastAPI()

# Define a Pydantic model for the sensor data
class SensorData(BaseModel):
    temperature: float
    humidity: float

# Define a route to get sensor data
@app.get("/sensor-data/", response_model=SensorData)
def get_sensor_data():
    # Simulate temperature and humidity data
    temperature = round(uniform(15.0, 30.0), 2)
    humidity = round(uniform(30.0, 70.0), 2)
    return {"temperature": temperature, "humidity": humidity}
