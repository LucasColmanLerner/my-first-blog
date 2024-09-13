import requests
username = 'lukecolman'
token = '31ca651f072051dd1c8f04d6f77d52d8efb31da6'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('Nos conectamos correctamente a python anywhere')
    print('CPU quota info:')
    print(response.content)
else:
    print("che no nos pudimos conectar")
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))