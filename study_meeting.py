import requests

if __name__ == '__main__':
    data = requests.get('http://connpass.com/api/v1/event/?keyword=python').json()
