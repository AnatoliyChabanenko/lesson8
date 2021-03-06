import requests
from bs4 import BeautifulSoup

class Iink_Iterator:
    URL = 'https://kmr.gov.ua/uk/stenogramu'
    def __init__(self ):

        self.index= 0
        self.mylen = 0
        self.dated = []
        self.mylink = []


    def get_page_content(self, url, attempts=3):
        if attempts < 0:
            raise Exception('No attempts')
        response = requests.get(url)
        if not response.ok:
            return self.get_page_content(url, attempts - 1)

        return BeautifulSoup(response.content, 'html.parser')

    def get_all_page(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text , 'html.parser')
        if soup.find('li', {'class': "pager-next"}):
            if soup.find('li', {'class': "pager-next"}).find('a'):
                d = soup.find('li', {'class': "pager-next"}).find('a').get('href')
                if d:
                    c = (Iink_Iterator.URL+d)
                    self.mylink.append(c)
                    print('op')
                    return self.get_all_page(c)
                else:
                    pass


    def get_document_links(self,soup):
        links = soup.findAll('div', {'class': "views-field views-field-title"})
        dates = soup.findAll('span', {'class': "date-display-single"})
        return dates, links


    def get_doc_from_page(self, soup) :
        dates, links = self.get_document_links(soup)
        for date, one_link in zip(dates, links):
            self.mylen += 1
            link = one_link.find('a', {'class': "field-content"}).get('href')
            title = one_link.find('span', {'class': "field-content"}).text
            filename = link.split('/')[-1]

            self.dated.append ([title, link,filename])



    def pase(self) :
        for i in self.mylink:
            page = self.get_page_content(i)
            self.get_doc_from_page(page)


    def __iter__(self):
        print('call')
        self.index = 0
        return self


    def __next__(self):
        if self.index >= self.mylen:
            raise StopIteration
        l = self.dated[self.index]
        self.index += 1
        return  l





if __name__ == '__main__':
    d = Iink_Iterator()
    d.get_all_page('https://kmr.gov.ua/uk/stenogramu')
    d.pase()
    for i in d:
        print(i)
    print(d.mylen)






