import csv


def output_to_csv(input_data, filename):
    data = filter_data(input_data)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['username', 'first_name', 'last_name', 'email', 'permissions', 'grn_permissions']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def filter_data(list_of_data):
    list_of_filtered_data = [{'username': data['username'], 'first_name': data['first_name'],
                              'last_name': data['last_name'], 'email': data['email'],
                              'permissions': data['permissions'], 'grn_permissions': data['grn_permissions']}
                             for data in list_of_data if '@officevnpay.com' in data['username']]

    return list_of_filtered_data
