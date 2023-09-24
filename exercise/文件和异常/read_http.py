import requests
import json

def main():
    resp = requests.get('https://reqres.in/api/users?page=2')
    data_model = json.loads(resp.text)
    # for news in data_model['newslist']:
    #     print(news['title'])
    # print(data_model)
    print(json.loads(resp.text))

if __name__ == '__main__':
    main()

# json.loads()：将 JSON 字符串转换为 Python 对象。
# resp.text：requests 库中 Response 对象的属性，返回 HTTP 响应的内容。
