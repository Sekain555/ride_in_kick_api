from pydantic import BaseModel

class ClimateData(BaseModel):
    temperature: float
    weather: str
    wind_speed: float
