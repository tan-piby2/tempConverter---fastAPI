from fastapi import FastAPI, HTTPException
from models import TemperatureConversionRequest, TemperatureConversionResponse, TemperatureUnit

app = FastAPI()

def convert_temperature(value: float, from_unit: TemperatureUnit, to_unit: TemperatureUnit) -> float:
    if from_unit == to_unit:
        return value

    # Convert from the original unit to Celsius
    if from_unit == TemperatureUnit.celsius:
        celsius_value = value
    elif from_unit == TemperatureUnit.fahrenheit:
        celsius_value = (value - 32) * 5 / 9
    elif from_unit == TemperatureUnit.kelvin:
        celsius_value = value - 273.15
    else:
        raise HTTPException(status_code=400, detail="Invalid temperature unit")

    # Convert from Celsius to the target unit
    if to_unit == TemperatureUnit.celsius:
        return celsius_value
    elif to_unit == TemperatureUnit.fahrenheit:
        return celsius_value * 9 / 5 + 32
    elif to_unit == TemperatureUnit.kelvin:
        return celsius_value + 273.15
    else:
        raise HTTPException(status_code=400, detail="Invalid temperature unit")

@app.post("/convert", response_model=TemperatureConversionResponse)
def convert_temperature_endpoint(request: TemperatureConversionRequest):
    converted_value = convert_temperature(request.value, request.from_unit, request.to_unit)
    return TemperatureConversionResponse(
        original_value=request.value,
        original_unit=request.from_unit,
        converted_value=converted_value,
        converted_unit=request.to_unit
    )

@app.get("/")
def read_root():
    return {"message": "Welcome to the Temperature Converter API!"}
