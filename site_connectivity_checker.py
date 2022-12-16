# import urllib
# use urllib.request to get the data from the url
# write a function that takes an url and then returns a response

import urllib.request as urllib

def connection_checker(url):
    print('Checking connectivity')
    response = urllib.urlopen(url)
    print(f'Connected to {url} successfully')
    print('The response code is', response.getcode())

print('This is a site connectivity checker program')
url = input('Enter the url: ')
connection_checker(url)