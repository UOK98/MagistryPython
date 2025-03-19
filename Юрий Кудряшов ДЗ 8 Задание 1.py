import requests
import json 

variable = requests.get('https://jsonplaceholder.typicode.com/posts')

variable = variable.json()

for post in variable[:5]: 
    print(f"Title: \n{post['title']}")
    print(f"Body: \n{post['body']}\n\n")