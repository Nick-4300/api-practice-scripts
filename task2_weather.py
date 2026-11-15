import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather_by_city():
    """Запрашивает город у пользователя и выводит текущую погоду."""
    if not API_KEY:
        print("Не найден OPENWEATHER_API_KEY. Создайте .env на основе .env.example.")
        return

    city_name = input("Введите название города на английском (например, London): ").strip()

    if not city_name:
        print("Название города не может быть пустым.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        print(f"\nПогода в городе {city_name}:")
        print(f"Температура: {temperature}°C")
        print(f"Описание: {description}")

    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            print("Ошибка авторизации. Проверьте API-ключ OpenWeather.")
        elif response.status_code == 404:
            print(f"Город '{city_name}' не найден. Попробуйте другое название.")
        else:
            print(f"HTTP-ошибка: {response.status_code}")
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при выполнении запроса: {error}")
    except KeyError:
        print("Не удалось извлечь данные о погоде из ответа API.")


if __name__ == "__main__":
    get_weather_by_city()