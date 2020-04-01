
email_dict = {}
email = input("Email: ")

while email != '':
    name = email.split('@')
    extract_name = name[0].split('.')
    final_name = ' '.join(extract_name).title()
    name_correct = input('Is your name {} (Y/n)'.format(final_name.title())).upper()
    if name_correct == 'Y' or name_correct == '':
        email_dict[final_name] = email
    elif name_correct == 'N':
        final_name = input("Name: ").title()
        email_dict[final_name] = email
    email = input("Email: ")

for names, emails in email_dict.items():
    print("{} ({})".format(names, emails))
