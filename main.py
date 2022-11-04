import requests


def main():
    params = {
        'text': 'NAME:Аналитик',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 1,  # Поиск ощуществляется по вакансиям города Москва
        'page': 2,  # Индекс страницы поиска на HH
        'per_page': 100  # Кол-во вакансий на 1 странице
    }
    url = 'https://api.hh.ru/vacancies'
    response = requests.get(url, params=params)
    response.raise_for_status()

    vacancy = response.content.decode()

    print(vacancy)


if __name__ == '__main__':
    main()
