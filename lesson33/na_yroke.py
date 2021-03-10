import requests
import dateutil.parser

import time


def unix_tame(date_str):
    return dateutil.parser.parse(date_str).strftime('%s')



def id_decl():
    url = 'https://public-api.nazk.gov.ua/v2/documents/list'
    data = {}
    while url:
        r = requests.get(url,params=data)
        if r.ok:

            if r.json().get('data'):

                for id,date in [(i.get('id'),i.get('date')) for i in r.json().get('data')]:
                    yield id
                data['end_date']=unix_tame(date)
            else:
                break
        else:
            time.sleep(2)




if __name__ == '__main__':
    for d in id_decl():
        print(d)