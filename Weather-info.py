import requests

# API key (replace with your own)
api_key = "YOUR_API_KEY"

# Location (replace with your own)
city = "New York"

# API endpoint
endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Send GET request to endpoint
response = requests.get(endpoint)

# Get data from response
data = response.json()

# Extract temperature from data
temp = data["main"]["temp"] - 273.15

# Extract humidity from data
humidity = data["main"]["humidity"]

# Extract weather description from data
description = data["weather"][0]["description"]

# Print the result
print(f"The weather in {city} is {description} with a temperature of {temp} C and humidity of {humidity}%")

