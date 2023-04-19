from time import sleep

import mechanize
import random
import string

url = "http://127.0.0.1:8000/auth/reg/"



abc = string.ascii_lowercase

for i in range(40):
    br = mechanize.Browser()
    br.set_handle_robots(False)  # ignore robots
    username = ''.join(random.sample(abc, random.randint(3, 15)))
    br.open(url)
    br.select_form(nr=0)
    br["username"] = username
    br["password1"] = '123'
    br["password2"] = '123'
    br["email"] = f'{username}@mail.ru'
    res = br.submit()
    print(f'Итерация {i} - завершена')
    sleep(1)

print('FINISED')