import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

BASE_URL = 'http://127.0.0.1:8000'

def read_route(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()
        return lines

def remote_control(route):
    url = f"{BASE_URL}/remote_control?route={route}"
    response = requests.get(url)
    return response.json()

def index():
    url = f"{BASE_URL}"
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':

    route = read_route('route.txt')
    remote_control = remote_control(route)
    logging.info(remote_control)

