import json
import requests
import os

BASE_ENDPOINT = 'http://127.0.0.1:8000/api/'
#REFRESH_ENDPOINT = AUTH_ENDPOINT+'refresh/'
#REGISTER_ENDPOINT = AUTH_ENDPOINT+'register/'

#img_path = os.path.join(os.getcwd(), "test_pic_1.png")

#Endpoint Request Examples:




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
print(r.text)
token=r.json()['token']
print(token)

# 2. refresh token
REFRESH_TOKEN_ENDPOINT = LOGIN_ENDPOINT+'refresh/'

refresh_headers = {
    'content-type': 'application/json',
    'Authorization': 'JWT '+token 
}
r=requests.post(REFRESH_TOKEN_ENDPOINT,headers = refresh_headers)
print(r.text)



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

#headers











'''

token = ""



def authMe():
    auth_data = {
        'username': 'admin',
        'password': '123456'
    }
    auth_headers = {
        'content-type': 'application/json',
    }
    auth_response = requests.post(AUTH_ENDPOINT, data=json.dumps(auth_data), headers=auth_headers)
    print('authMe')
    print(auth_response)
    return auth_response


def refreshMe(token):
    refresh_headers = {
        'content-type': 'application/json',
        'Authorization': 'JWT '+token
    }
    refresh_response = requests.post(REFRESH_ENDPOINT, headers=refresh_headers)
    print('refreshMe')
    print(refresh_response)
    return refresh_response


def gt_auth(token):
    if token == "":
        response=authMe()
        status=response.status_code
        if status==200:
            return response.json()['token']
        else:
            return ""
    else:
        response=refreshMe(token)
        status=response.status_code
        if(status==200):
            return response.json()['token']
        else:
            response=authMe()
            status=response.status_code
            if status==200:
                return response.json()['token']
            else:
                return ""

token=gt_auth(token)
print(token)
token=gt_auth(token)
print(token)

ALL_PROFILE_ENDPOINT = 'http://127.0.0.1:8000/api/profile/'
user = 25

update_data ={
    'about': 'How Much or?',
    'rating': '1500',
}

update_headers={
    'Authorization': 'JWT '+token,
}

update_response = requests.put(ALL_PROFILE_ENDPOINT+str(user)+'/', data=update_data, headers=update_headers)
print(update_response.text)

delete_response = requests.delete(ALL_PROFILE_ENDPOINT+str(user)+'/', headers=update_headers)
print(delete_response.status_code)
'''



'''
register_data = {
    'username': 'iefwfawfwfeeadmon',
    'email': 'awfwafwfawaweqeqseg@site.com',
    'first_name': 'KK Korimon',
    'last_name': 'Banu BB',
    'password': '123456',
    'confirm_password': '123456',
}

req_req = requests.post(REGISTER_ENDPOINT, data=json.dumps(register_data), headers=headers)
print(req_req.text)
'''
'''
headers = {
    'content-type': 'application/json',
    'Authorization': 'JWT '+'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMywidXNlcm5hbWUiOiJpZXNlZ3dlZWFkbW9uIiwiZXhwIjoxNTk3OTI4MjI1LCJlbWFpbCI6ImF3ZndhZmVxZXFzZWdAc2l0ZS5jb20iLCJvcmlnX2lhdCI6MTU5NzkyNzkyNX0.TU78R9k2M-R3Jed51FvdVMUGsnXd9GKZs3cth-iWax0',
}

admin_data = {
    'username': 'admin@site.com',
    'password': '123456',
}
'''

'''
admin2_data = {
    'username': 'admin2',
    'password': '123456',
}
'''
#r = requests.post(AUTH_ENDPOINT, data=json.dumps(admin_data), headers=headers)
#r2 = requests.post(AUTH_ENDPOINT, data=json.dumps(admin2_data), headers=headers)

#token = r.json()
#token = r.json()['token']
#token2 = r2.json()['token']
#print(r.text)
#print(token2)

'''
headers ={
    'content-type': 'application/json',
    'Authorization': 'JWT '+token,
}

data ={
    'about': "this is about",
    'rating': 1400,
}

r_admin = requests.post(ENDPOINT,data=json.dumps(data), headers=headers);
print(r_admin.text)


headers2 = {
    "Authorization": "JWT "+token2,
    #'content-type': 'application/json',
}

with open(img_path, 'rb') as image:
    file_data = {
        'image': image #'serializer_field_name': name_of_image_here
    }
    data = {
        "about": "Hola, tomar lungi khola.",
        "rating": 1453,
    }
    posted_response = requests.post(ENDPOINT, data=data, headers=headers2, files=file_data)
    print(posted_response.text)

headers2 = {
    "Authorization": "JWT "+token2,
    'content-type': 'application/json',
}
data = {
        "about": "Aikkawala bas",
        "rating": 4500,
    }
posted_response = requests.put(ENDPOINT + str(2) +'/', data=json.dumps(data), headers=headers2)
print(posted_response.text)

posted_response = requests.delete(ENDPOINT + str(2)+'/', headers=headers2)
print(posted_response.text)



'''
'''
print(token)

data = {
    'token': token
}

r = requests.post(AUTH_REFRESH_ENDPOINT, data=json.dumps(data), headers = headers)
token = r.json()['token']
print(token)


get_endpoint= ENDPOINT+str(1)
post_data= json.dumps({'about': "fuck the tutorials"})

r = requests.get(get_endpoint)
print(r.text)

r2 = requests.get(ENDPOINT)
print(r2.status_code)

post_headers = {
    'content-type': 'application/json'
}

post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
print(post_response.text)

def do_img(method='get', data={}, is_json=True, image_path=None):
    headers = {}
    if is_json == True:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if image_path is not None:
        with open(img_path, 'rb') as image:
            file_data = {
                'image': image #'serializer_field_name': name_of_image_here
            }
            r = requests.request(method, ENDPOINT, data=data, headers=headers, files=file_data)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

#do_img(method='post', data={'user': 3, 'about': 'hi', 'rating': 1422}, is_json=False, image_path=img_path)
do_img(method='put',data={'user': 4, "about": "What the fuck 2?", "rating": 1444}, is_json=False, image_path=img_path)


def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json == True:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


#do(method='post',data={'user': 1, "about": "hi", "rating": 1422})
#do(data={'user': 1})
#do(method='put',data={'user': 1, "about": "What the fuck 2?", "rating": 1444})
#do(method='patch',data={'user': 1 , "about": "Hello Jonogon", "rating": 1622})
#do(method='delete',data={'user': 1})

'''