import requests
from bs4 import BeautifulSoup

HOST = 'https://kmr.gov.ua'
URL = 'https://kmr.gov.ua/uk/stenogramu'
HEADERS= {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36', 'accept': '*/*'}

d = '<a href="/uk/file/157173/download?token=YZ1B3-VvpEV43QzdNpyPt_0Kx7WXveCcREr3Y_Voudg" class="format odt field-content" size_eye="11">doc</a>'
def get_htms(url , params= None):
    r = requests.get(url, headers = HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html , 'html.parser')
    items = soup.find_all('a',class_= 'format odt field-content' )
    links_to_download= []
    for item in items:
        links_to_download.append(HOST + item.get('href'))
    return links_to_download

def pase():
    html = get_htms(URL)
    if html.status_code == 200:
        fd= []
        pages_cou = get_pages_cou(html.text)
        for page in range(1, pages_cou + 1):
            print(f'{page}')
            html = get_htms(URL, params={'page': page})
            fd.extend(get_content(html.text))

        return fd
    else:
        print('ошибочка')

def download_file(file_link, folder):
    name = file_link.split('/')[-1]
    save_path = folder + name
    r = requests.get(file_link, allow_redirects=True)
    print("Saving file:", save_path)
    with open(name, 'wb') as fp:
        fp.write(r.content)

def get_pages_cou(html):
    soup = BeautifulSoup(html , 'html.parser')
    pagis = soup.find_all('li',class_= 'pager-item')
    if pagis:
        return int(pagis[-1].get_text())
    else:
        return 1

if __name__ == '__main__':
    d = pase()
    print(d)
    # for link in d:
    #     download_file(link,'lesson31')

