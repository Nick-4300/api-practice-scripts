# API Practice Scripts

Учебный проект с двумя скриптами для работы с публичными API.

## Скрипты

- `task1_posts.py` — получает первые 5 постов из JSONPlaceholder.
- `task2_weather.py` — получает текущую погоду по названию города через OpenWeather API.

## Установка

1. Скачайте архив репозитория (`Code → Download ZIP`) или клонируйте репозиторий, если у вас установлен Git:

```bash
git clone https://github.com/ВАШ_ЛОГИН/api-practice-scripts.git
cd api-practice-scripts
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` на основе `.env.example`:

```bash
cp .env.example .env
```

Windows:

```bash
copy .env.example .env
```

5. Получите бесплатный API-ключ OpenWeather: https://openweathermap.org/api

6. Вставьте ключ в `.env`:

```env
OPENWEATHER_API_KEY=ваш_ключ_здесь
```

## Запуск

Задание 1:

```bash
python task1_posts.py
```

Задание 2:

```bash
python task2_weather.py
```
