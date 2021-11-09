import requests
from datetime import  datetime
USERNAME = "akanksha"
TOKEN = "asdfghjkl1234"
GRAPHID = "graph1"

now = datetime.now()
today_date = now.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
pixel_params = {
    "date": today_date,
    "quantity": input("How many hours did you code today? "),
}
pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"
put_endpoint = f"{pixel_endpoint}/{today_date}"

put_params = {
    "quantity": "3",
}

# PUT
# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)

# Request for updation
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

# DELETE
# response = requests.delete(url=put_endpoint, headers=headers)
# print(response.text)



