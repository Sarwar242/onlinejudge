import json
import requests
import os

BASE_ENDPOINT = 'http://127.0.0.1:8000/api/profile/'
user1 = 1
user2 = 2

# 1. All View Profiles
r=requests.get(BASE_ENDPOINT)
print(r.text)

# 2. View by profile by user
PROFILE_ENDPOINT = BASE_ENDPOINT+str(user2)+'/'
r=requests.get(PROFILE_ENDPOINT)
print(r.text)


# (login first)
LOGIN_ENDPOINT = 'http://127.0.0.1:8000/api/auth/'

login_data = {
    'username': 'admin',
    'password': '123456',
}

login_headers = {
    'content-type': 'application/json',
}

login_r = requests.post(LOGIN_ENDPOINT, data=json.dumps(login_data), headers=login_headers)
token = login_r.json()['token']




# 3. Create profile
#user one of the two img_path to update with or without image
img_path = None
#img_path = os.path.join(os.getcwd(), "test_pic_1.png")

create_data = {
    'mobile_no': '+8801753537110',
    'google_id': 'jbawjfha',
    'institution_id': '1',
}

create_headers = {
    'Authorization': 'JWT '+token,
}

if img_path is not None:
    with open(img_path, 'rb') as image:
        file_data = {
            'have_profile_image': image,
        }
        r = requests.post(BASE_ENDPOINT, data=create_data, headers=create_headers, files=file_data)
        print(r.text)
else:
    r = requests.post(BASE_ENDPOINT, data=create_data, headers=create_headers)
    print(r.text)



# 3. Update user
PROFILE_ENDPOINT = BASE_ENDPOINT+str(user1)+'/'
#user one of the two img_path to update with or without image
#img_path = None
img_path = os.path.join(os.getcwd(), "test_pic_1.png")

update_data = {
    'mobile_no': '+8801111111111',
    'google_id': 'jbawjfhalwfalfwlawhfl',
    'institution_id': 2,
}

update_headers = {
    'Authorization': 'JWT '+token,
}

if img_path is not None:
    with open(img_path, 'rb') as image:
        file_data = {
            'have_profile_image': image,
        }
        r = requests.put(PROFILE_ENDPOINT, data=update_data, headers=update_headers, files=file_data)
        print(r.text)
else:
    r = requests.put(PROFILE_ENDPOINT, data=update_data, headers=update_headers)
    print(r.text)

# 4. Delete user
delete_headers = {
    'Authorization': 'JWT '+token,
}
r=requests.delete(PROFILE_ENDPOINT, headers=delete_headers)
status = r.status_code
if status == 204:
    print('Successfully deleted.')
else:
    print(r.text)
