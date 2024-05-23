import requests
from bs4 import BeautifulSoup


def get_google_search_a(query):
    try:
        url = f"https://www.google.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        data = soup.find_all('a')
        l = []
        for x in data:
            # print(x)
            # print(x["href"])
            # print(10 * '*')
            l.append({'href': x['href'], 'data': x})
        print(l)
    except Exception as e:
        return e

def get_links(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    l = []
    for link in soup.find_all('a'):
        l.append([link.get('href')])
    return l


def get_many_info(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # titulo = soup.title
    info = soup.text
    info_splited = info.split("›")
    l = []
    for data in info_splited: l.append([data])
    print(l)
    return l


if __name__ == "__main__":
    # user_query = input("Digite o que deseja pesquisar no Google: ")
    query_ = 'Google foi vendida para o Elon Musk'
    # get_google_search_a(query_)
    get_many_info(query_)
    # print(get_links(query_))
