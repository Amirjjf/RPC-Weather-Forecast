import grpc
import weather_pb2
import weather_pb2_grpc
from concurrent import futures
import requests

# Replace with your real API Key from OpenWeatherMap
API_KEY = "Your API Key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class WeatherService(weather_pb2_grpc.WeatherServiceServicer):
    def GetWeather(self, request, context):
        city = request.city
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()

        if response.get("cod") != 200:
            return weather_pb2.WeatherResponse(
                city=city, temperature="N/A", description="City not found", humidity="N/A"
            )

        return weather_pb2.WeatherResponse(
            city=city,
            temperature=f"{response['main']['temp']} °C",
            description=response["weather"][0]["description"],
            humidity=f"{response['main']['humidity']}%"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherService(), server)
    server.add_insecure_port("[::]:50051")
    print("Weather gRPC Server is running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()