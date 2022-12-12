# collect the email from user
# split the email using the @, the first part is the user name
# the second part is the domain
# split the domain use ., the first part is the domain name
# the second part is the extension
def main():
    print('\nWelcome to the email slicer')
    print('')

    email_input = input('Input your email address: ')
    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')

    print(f'Username : {username}')
    print(f'Domain : {domain}')
    print(f'Extension: {extension}')

while True:
    main()