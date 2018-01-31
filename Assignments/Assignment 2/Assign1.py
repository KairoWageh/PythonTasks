import random
import webbrowser

websites = ['Google','Yahoo','Facebook']
website = random.choice(websites)
url = ''
def websites(website):
    print(website)
    if(website == 'Google'):
        url = 'https://google.com'
        web = webbrowser.open_new(url)
        #print('Google is opened')
    elif(website == 'Yahoo'):
        url = 'https://www.yahoo.com'
        web = webbrowser.open_new(url)
        #print('Yahoo is opened')
    elif(website == 'Facebook'):
        url = 'https://www.facebook.com'
        web = webbrowser.open_new(url)
        #print('Facebook is opened')
    return (web)
