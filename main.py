from fastapi import FastAPI
from app.models import ClimateData
from app.gpt_model import generate_advice

app = FastAPI()

@app.post("/climate-advice/")
async def get_climate_advice(climate_data: ClimateData):
    temperature = climate_data.temperature
    weather = climate_data.weather
    wind_speed = climate_data.wind_speed

    # Crear un prompt basado en los datos climáticos
    prompt = (
        f"Genera un consejo para conducir basado en los siguientes datos climáticos: "
        f"Temperatura: {temperature}°C, Clima: {weather}, Velocidad del viento: {wind_speed} km/h."
    )
    
    # Usar el modelo para generar un consejo
    advice = generate_advice(prompt)

    print(generate_advice)
    
    return {"advice": advice}
