import graylog


def create_a_new_user(url, token, list_of_user):
    filtered_user_list = filter_user_list(list_of_user)
    for user in filtered_user_list:
        new_username = user['username'].replace('@officevnpay.com', '')
        res = graylog.create_user(url, token, new_username, user['permissions'], user['roles'])

        if res.status_code == 201:
            print("[{} {}] Created user {} successfully.".format(res.status_code, res.reason, new_username))
        else:
            print("[{} {}] {}".format(res.status_code, res.reason, res.json()['message']))


def filter_user_list(list_of_user):
    filtered_user_list = [user for user in list_of_user if '@officevnpay.com' in user['username']]
    return filtered_user_list

