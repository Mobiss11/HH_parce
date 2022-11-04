import requests


def main():
    params = {
        'text': 'NAME:Разработчик',
        'area': 1,
        'page': 2,
        'per_page': 100,
        'date_format': '2022-11-04',
    }
    url = 'https://api.hh.ru/vacancies'
    response = requests.get(url, params=params)
    response.raise_for_status()

    vacancy = response.content.decode()

    print(vacancy)


if __name__ == '__main__':
    main()
