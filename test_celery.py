import requests


def test_celery():
    requests.get('http://0.0.0.0:8000/hello-world?name=Vitalii')
    requests.get('http://0.0.0.0:8000/hello-world?name=Ivan')
    requests.get('http://0.0.0.0:8000/hello-world?name=Vlad')
    requests.get('http://0.0.0.0:8000/hello-world?name=Oleg')
    requests.get('http://0.0.0.0:8000/hello-world?name=Igor')
    requests.get('http://0.0.0.0:8000/hello-world?name=Vladimir')
    requests.get('http://0.0.0.0:8000/hello-world?name=Vasyl')
    requests.get('http://0.0.0.0:8000/hello-world?name=Olena')


if __name__ == '__main__':
    test_celery()
