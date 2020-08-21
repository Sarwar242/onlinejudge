import json
import requests
import os

BASE_ENDPOINT = 'http://127.0.0.1:8000/api/'

#img_path = os.path.join(os.getcwd(), "test_pic_1.png")

#Endpoint Request Examples:

token = ""


# 1. Login
LOGIN_ENDPOINT = BASE_ENDPOINT+'auth/'

login_data_1 = {
    'username': 'admin',
    'password': '123456',
}

login_data_2 = {
    'username': 'admin@site.com',
    'password': '123456',
}

login_headers = {
    'content-type': 'application/json',
}

r=requests.post(LOGIN_ENDPOINT,data=json.dumps(login_data_1),headers=login_headers)
print('Login Response with username: ')
print(r.text)
if r.status_code==200:
    token=r.json()['token']
    print('Login Token: ')
    print(token)
else:
    print(r.status_code)

r=requests.post(LOGIN_ENDPOINT,data=json.dumps(login_data_2),headers=login_headers)
print('Login Response with Email: ')
print(r.text)
if r.status_code==200:
    token=r.json()['token']
    print('Login Token: ')
    print(token)
else:
    print(r.status_code)



# 2. refresh token
REFRESH_TOKEN_ENDPOINT = LOGIN_ENDPOINT+'refresh/'

refresh_data = {
    'token': token,
}

refresh_headers = {
    'content-type': 'application/json',
}
r=requests.post(REFRESH_TOKEN_ENDPOINT,data=json.dumps(refresh_data), headers = refresh_headers)
print('Refresh Token Response: ')
print(r.text)
token = r.json()['token']
print('Refreshed Token: ')
print(token)

# 3. Register user
REGISTER_ENDPOINT = LOGIN_ENDPOINT+'register/'

register_data = {
    'username': 'yourname',
    'email': 'yourmail@mail.com',
    'first_name': 'Your First Name',
    'last_name': 'Your Last Name',
    'password': 'this_is_your_password',
    'confirm_password': 'this_is_your_password'
}

authenticated_headers = {
    'content-type': 'application/json',
    'Authorization': 'JWT '+token
}

annonemous_headers = {
    'content-type': 'application/json',
}

r = requests.post(REGISTER_ENDPOINT, data=json.dumps(register_data), headers=authenticated_headers)
print('Registration request Response for Authenticated user: ')
print(r.text)

r = requests.post(REGISTER_ENDPOINT, data=json.dumps(register_data), headers=annonemous_headers)
print('Registration request Response for Annonemous user: ')
print(r.text)