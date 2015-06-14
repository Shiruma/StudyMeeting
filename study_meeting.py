import requests

if __name__ == '__main__':
    data = requests.get('http://connpass.com/api/v1/event/?keyword=python').json()
    events = data['events']
    for event in events:
        print(event['title'])