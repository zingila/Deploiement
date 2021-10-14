import os
import requests
import time

#Refresh the page
time.sleep(3)

api_address = "fastapi"
api_port = 8000

r = requests.get(url="http://{address}:{port}/prediction".format(address=api_address, port=api_port), params= {
    "username": "alice",
    "password": "wonderland"
})

output = '''
============================
    Authentication test
============================

request done at "/prediction"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(status_code=status_code, test_status=test_status)

# impression dans un fichier
if os.environ.get('LOG') == "1":
    with open('api_test.log', 'a') as file:
        file.write(output)

r_2 = requests.get(url="http://{address}:{port}/prediction".format(address=api_address, port=api_port), params= {
    "username": "bob",
    "password": "builder"
})

output_2 = '''
============================
    Authentication test
============================

request done at "/prediction"
| username="bob"
| password="builder"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code_2 = r_2.status_code

# affichage des résultats
if status_code_2 == 200:
    test_status_2 = 'SUCCESS'
else:
    test_status_2 = 'FAILURE'
output_2 = output_2.format(status_code=status_code_2, test_status=test_status_2)

# impression dans un fichier
if os.environ.get('LOG') == "1":
    with open('api_test.log', 'a') as file:
        file.write(output_2)

r_3 = requests.get(url="http://{address}:{port}/prediction".format(address=api_address, port=api_port), params= {
    "username": "clementine",
    "password": "mandarine"
})

output_3 = '''
============================
    Authentication test
============================

request done at "/prediction"
| username="clementine"
| password="mandarine"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code_3 = r_3.status_code

# affichage des résultats
if status_code_3 == 200:
    test_status_3 = 'SUCCESS'
else:
    test_status_3 = 'FAILURE'
output_3 = output_3.format(status_code=status_code_3, test_status=test_status_3)

# impression dans un fichier
if os.environ.get('LOG') == "1":
    with open('api_test.log', 'a') as file:
        file.write(output_3)

print("Le container authentification: fonctionnelle")
#print(os.environ.get('LOG'))
