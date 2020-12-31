import requests
import os

query = input("Enter the waifu name: ")

r = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 200,
        'q': query,
        't': 'images',
        'safesearch': 0,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 '
    }
)

os.makedirs(query, exist_ok=True)
response = r.json().get('data').get('result').get('items')
print(r)
urls = [r.get('media') for r in response]
for i in range(len(urls)):
    print(urls[i])
    img_data = requests.get(urls[i]).content
    with open("./"+query+"/"+str(i)+'.jpg', 'wb') as handler:
        handler.write(img_data)
