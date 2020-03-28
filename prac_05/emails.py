
email_dict = {}
email = input("Email: ")
#email = "susan.morton@jcu.edu.au"

while email != '':
    #email = input("Email: ")
    #email = "susan.morton@jcu.edu.au"
    name = email.split('@')
    print(name)
    extract_name = name[0].split('.')
    print(extract_name)
    final_name = ' '.join(extract_name)
    print(final_name.title())
    name_correct = 'Y'
    name_correct = input('Is your name {} (Y/n)'.format(final_name.title())).upper()
    if name_correct == 'Y':
        print('yay')
        email_dict[final_name] = email
    elif name_correct =='N':
        print('boo')
        final_name = input("Name: ").title()
        email_dict[final_name] = email
    email = input("Email: ")


print(email_dict)


