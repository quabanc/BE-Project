import requests
url = 'http://127.0.0.1:5000/upload'
files = {'image': open('test_imgs/dog.jpg', 'rb')}
requests.post(url, files=files)