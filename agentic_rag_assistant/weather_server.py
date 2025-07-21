from fastmcp import FastMCP
import random

known_weather_data = {
    "berlin": 20.0
}

mcp = FastMCP("Weather Server 🌦️")

@mcp.tool
def get_weather(city: str) -> float:
    """
    Retrieves the temperature for a specified city.
    """
    city = city.strip().lower()
    if city in known_weather_data:
        return known_weather_data[city]
    return round(random.uniform(-5, 35), 1)

@mcp.tool
def set_weather(city: str, temp: float) -> str:
    """
    Sets the temperature for a specified city.
    """
    city = city.strip().lower()
    known_weather_data[city] = temp
    return "OK"

if __name__ == "__main__":
    mcp.run()