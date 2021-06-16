import requests
# loading a page 
data=requests.get('https://rancher.com/')
# checking exit code
print(data.status_code)
# to print back URL 
print(data.url)
# original html code data 
print(data.content)
print(data.text)
