import requests


def fetch_and_print_posts():
    """Загружает и выводит заголовки и тела первых 5 постов."""
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        posts = response.json()

        for index, post in enumerate(posts[:5], start=1):
            print(f"Пост #{index}")
            print(f"Заголовок: {post['title']}")
            print(f"Тело: {post['body']}")
            print("-" * 40)

    except requests.exceptions.RequestException as error:
        print(f"Ошибка при выполнении запроса: {error}")


if __name__ == "__main__":
    fetch_and_print_posts()