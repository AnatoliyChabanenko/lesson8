import requests
from bs4 import BeautifulSoup


class Iink_Iterator:
    def __init__(self, url):
        self.url = url
        self.index = 0
        self.mylen = 0
        self.dated = []

    def get_page_content(self, url, attempts=3):
        if attempts < 0:
            raise Exception('No attempts')
        response = requests.get(self.url)
        if not response.ok:
            return self.get_page_content(self.url, attempts - 1)

        return BeautifulSoup(response.content, 'html.parser')

    def get_next_page(self, page):
        if page.find('li', {'class': "pager-next"}):
            if page.find('li', {'class': "pager-next"}).find('a'):
                return page.find('li', {'class': "pager-next"}).find('a').get('href')

    def get_document_links(self, soup):
        links = soup.findAll('div', {'class': "views-field views-field-title"})
        dates = soup.findAll('span', {'class': "date-display-single"})
        return dates, links

    def get_doc_from_page(self, soup):
        dates, links = self.get_document_links(soup)
        for date, one_link in zip(dates, links):
            self.mylen += 1
            link = one_link.find('a', {'class': "field-content"}).get('href')
            title = one_link.find('span', {'class': "field-content"}).text
            filename = link.split('/')[-1]
            self.dated.append([title, link, filename])

    def get_kmr_documents(self):

        page = self.get_page_content(self.url)
        self.get_doc_from_page(page)
        for doc in self.dated:
            return doc
        page = self.get_next_page(page)

    def __iter__(self):
        print('call')
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.mylen:
            raise StopIteration
        lena = self.dated[self.index]
        self.index += 1
        return lena


if __name__ == '__main__':
    d = Iink_Iterator('https://kmr.gov.ua/uk/stenogramu')
    d.get_kmr_documents()
    print(next(d))
    print(next(d))

    print(d.mylen)
