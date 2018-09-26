from robobrowser import RoboBrowser
import time
from requests import Session

session = Session()
browser = RoboBrowser(history=True, user_agent='Safari 9.0',parser='html.parser',session=session)
browser.open('https://m.facebook.com/login.php',)

form = browser.get_form(id='login_form')



form['email'].value = 'emample@gmail.com'
form['pass'].value = '*****************'

browser.submit_form(form,submit=form['login'])

print(form)
print('Login Aplied')
print(browser.parsed)
next = browser.url
browser.open(next)
print(browser.parsed)

next_f = browser.get_forms()[0]
print(next_f)
uu = input()
if uu == 'y':
    browser.submit_form(next_f, submit=next_f['submit[Continue]'])
else:
    exit()


time.sleep(5)

next = browser.url

print(next)
loop = 0

while True:
    if loop % 2 == 0:
        browser.open('https://m.facebook.com/')
    else:
        browser.open('https://m.facebook.com/messages')

    print('Browsing '+str(loop)+' Times')
    loop += 1
    time.sleep(10)

