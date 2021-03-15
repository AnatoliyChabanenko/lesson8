import requests
import multiprocessing
import json




def get_content(url):
    ret = requests.get(url)
    data = ret.json()
    return data

def get_coments(data):
    comments = []
    for entry in data[ 'data']:
        comment = {'autor':entry['author'],'time':entry['created_utc'], 'text':entry['body']}
        comments.append(comment)
    return comments

def write_data_to_fail(data):

    with open('commend.json', 'w') as f:
        json.dump(data, f)

def load_(url):

    data = get_content(url)
    comments = get_coments(data)
    write_data_to_fail(comments)




if __name__ == '__main__':
    url = 'https://api.pushshift.io/reddit/comment/search/'
    t = multiprocessing.Process(target=load_, args= (url,) )
    t.start()
    print('start')
    t.join()
    print('c')



