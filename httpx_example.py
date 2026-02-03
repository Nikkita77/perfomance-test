from pprint import pprint

import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response)
# print(response.json())
#
# data = {
#     "title": "РќРѕРІР°СЏ Р·Р°РґР°С‡Р°",
#     "completed": False,
#     "userId": 1
# }
# response = httpx.post("https://jsonplaceholder.typicode.com/todos")
#
# print(response.status_code)
# print(response.json())
#
# """РџРµСЂРµРґР°С‡Р° С‚РѕРєРµРЅР° РІ С…РµРґРµСЂР°С…"""
# headers = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
#
# print(response.status_code)
# print(response.request.headers)
# print(response.headers)
#
# """РџРµСЂРµРґР°С‡Р° query РїР°СЂР°РјРµС‚СЂРѕРІ РІ  СѓСЂР»Рµ"""
# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#
# print(response.status_code)
# pprint(response.json())

# """РџРµСЂРµРґР°С‡Р° С„Р°Р№Р»Р° СЃ РµРіРѕ РїСЂРµРѕР±СЂР°Р·РѕРІР°РЅРёРµРј РІ С‚РµРєСЃС‚"""
#
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print(response.json())  # РћС‚РІРµС‚ СЃ РґР°РЅРЅС‹РјРё Рѕ Р·Р°РіСЂСѓР¶РµРЅРЅРѕРј С„Р°Р№Р»Рµ

with httpx.Client(
    base_url="https://jsonplaceholder.typicode.com",
    headers={"Authorization": "Bearer my secret_token"},
) as client:
    response1 = client.get("/todos/1")
    response2 = client.get("/todos/2")
    response1.raise_for_status()
    response2.raise_for_status()

    print(response1.status_code)
    print(response1.json())  # Р”Р°РЅРЅС‹Рµ РїРµСЂРІРѕР№ Р·Р°РґР°С‡Рё
    print(response2.status_code)
    print(response2.json())  # Р”Р°РЅРЅС‹Рµ РІС‚РѕСЂРѕР№ Р·Р°РґР°С‡Рё
