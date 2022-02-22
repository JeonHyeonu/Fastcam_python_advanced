import re
from unittest import result

regex = re.compile('^[\w-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

datas = [
    'startcoding@maver.com',
    'start-coding@maver.com',
    'start_coding@maver.co.kr',
    'startcoding@k-mail.com',
    '@maver.com',
    'startcoding?@k-mail.com',
    'startcoding@k-mail',
    'startcoding@maver'
]

for data in datas:
    matchoj = regex.match(data)
    result = (lambda x : True if x != None else False)(matchoj)
    print(f'{data} [{result}]')