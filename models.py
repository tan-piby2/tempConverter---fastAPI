from pydantic import BaseModel
from enum import Enum

class TemperatureUnit(str, Enum):
    celsius = "celsius"
    fahrenheit = "fahrenheit"
    kelvin = "kelvin"

class TemperatureConversionRequest(BaseModel):
    value: float
    from_unit: TemperatureUnit
    to_unit: TemperatureUnit

class TemperatureConversionResponse(BaseModel):
    original_value: float
    original_unit: TemperatureUnit
    converted_value: float
    converted_unit: TemperatureUnit
