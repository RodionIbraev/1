from bs4 import BeautifulSoup
import requests


URL = "https://habr.com/ru/all/"


def main():
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    keywords = [word for word in input('Введите ключевые слова через пробел:\n').split()]
    for i in soup.find_all("div", "tm-article-snippet"):
        check = False
        for key in keywords:
            if i.text.find(key) != -1:
                check = True
                break
        if check:
            time = i.find("time").attrs['title']
            title = i.find("h2", "tm-article-snippet__title tm-article-snippet__title_h2").span.text
            href = 'https://habr.com' + i.find("h2", "tm-article-snippet__title tm-article-snippet__title_h2").a.attrs['href']
            print('{} - {} - {}'.format(time, title, href))
            check = False


if __name__ == "__main__":
    main()