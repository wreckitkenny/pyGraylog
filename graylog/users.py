import requests
import json


def create_user(url, token, username, list_of_perms, list_of_roles):
    url = url + '/api/users'
    token = (token, 'token')
    headers = {'content-type': 'application/json', 'X-Requested-By': 'pyGraylog'}
    body = {'username': username,
            'email': username + '@vnpay.vn',
            'first_name': username,
            'last_name': username,
            'password': 'Gr4yL0g@123',
            'permissions': list_of_perms,
            'roles': list_of_roles}
    res = requests.post(url=url, auth=token, headers=headers, data=json.dumps(body))

    return res


def get_user(url, token, user):
    url = url + '/api/users/{}'.format(user)
    token = (token, 'token')
    headers = {'content-type': 'application/json'}
    res = requests.get(url=url, auth=token, headers=headers)

    return res.json()


def list_all_user(url, token, include_permissions, include_sessions):
    url = url + '/api/users'
    token = (token, 'token')
    headers = {'content-type': 'application/json'}
    params = {'include_permissions': include_permissions, 'include_sessions': include_sessions}
    res = requests.get(url=url, auth=token, headers=headers, params=params)

    return res.json()


