import os
import sys
import graylog
import argparse


def helper():
    parser = argparse.ArgumentParser(description="Graylog User Script")
    parser.add_argument('-u', '--user', help='Get a specific user')
    parser.add_argument('-a', '--all', help='List all users', action='store_true')
    parser.add_argument('-c', '--create', help='Create an user')
    parser.add_argument('-p', '--permission', help='Include user\'s permissions', action='store_true')
    parser.add_argument('-s', '--session', help='Include user\'s sessions', action='store_true')
    parser.add_argument('-o', '--output', help='Output to a csv file')
    parser.add_argument('-m', '--migrate', help='Migrate LDAP user to normal user', action='store_true')
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
    else:
        return args


def main():
    args = helper()
    url = os.getenv('GRAYLOG_URL')
    token = os.getenv('GRAYLOG_TOKEN')
    if args.all:
        list_of_user = graylog.list_all_user(url, token, args.permission, args.session)
        if args.output is not None:
            graylog.output_to_csv(list_of_user['users'], args.output)
        elif args.migrate:
            graylog.create_a_new_user(list_of_user['users'])
        else:
            print(list_of_user)
    if args.user is not None:
        user_info = graylog.get_user(url, token, args.user)
        if args.output is not None:
            graylog.output_to_csv([user_info], args.output)
        elif args.migrate:
            graylog.create_a_new_user([user_info])
        else:
            print(user_info)


if __name__ == '__main__':
    main()
