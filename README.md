# Weather Forecast RPC System

This project implements a **gRPC-based Remote Procedure Call (RPC) system** to fetch real-time weather data.

## Requirements
- Python 3.7+
- Install dependencies:
  pip install grpcio grpcio-tools requests  

## Setup
1. **Generate gRPC code** (only needed if modifying `weather.proto`):
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. weather.proto

2. **Start the gRPC Server**:
   python weather_server.py

3. **Run the gRPC Client**:
   python weather_client.py

   Enter a city name when prompted.

## Example Output
Enter city name: Paris
City: Paris
Temperature: 18°C
Weather: clear sky
Humidity: 60%

## Notes
- Requires an **OpenWeatherMap API Key** (replace `"your api key"` in `weather_server.py`).
- Ensure **port 50051** is available for gRPC communication.
