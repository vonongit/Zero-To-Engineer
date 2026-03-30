def main():
    users = get_data(user_url)

    with open('user.csv', 'w', newline='') as f:
        writer = csv.writer(f)
    for user in users:
        name = user['name']
        email = user['email']
        city = user['address']['city']
        comp_name = user['company']['name']
        writer.writerow([name, email, city, comp_name])

if __name__ == '__main__':
    main()