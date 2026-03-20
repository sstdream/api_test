import requests
import json

def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200, f"状态码错误：{response.status_code}"
    data = response.json()
    assert data['id'] == 1, f"id错误：{data['id']}"
    print("测试通过！")

if __name__ == "__main__":
    test_get_post()
