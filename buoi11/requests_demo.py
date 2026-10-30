import requests

"""
response = requests.get("https://api.github.com/repos/python/cpython")
if response.status_code == 200:
    du_lieu = response.json()
    print("Ten repository:", du_lieu["full_name"])
    print("So luot gan sao (stars):", du_lieu["stargazers_count"])
    print("Ngon ngu chinh:", du_lieu["language"])
else:
    print("Goi API that bai, ma loi:", response.status_code)
"""

response = requests.get("https://open.er-api.com/v6/latest/USD")

if response.status_code == 200:
    du_lieu = response.json()
    ty_gia_vnd = du_lieu["rates"]["VND"]
    print(f"1 USD = {ty_gia_vnd:,.0f} VND")
else:
    print("Khong lay duoc ty gia, ma loi", response.status_code)