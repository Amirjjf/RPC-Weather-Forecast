import grpc
import weather_pb2
import weather_pb2_grpc

def get_weather(city):
    channel = grpc.insecure_channel("localhost:50051")
    stub = weather_pb2_grpc.WeatherServiceStub(channel)

    request = weather_pb2.WeatherRequest(city=city)
    response = stub.GetWeather(request)

    print(f"City: {response.city}")
    print(f"Temperature: {response.temperature}")
    print(f"Weather: {response.description}")
    print(f"Humidity: {response.humidity}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
