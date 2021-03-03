import requests

url = 'http://csbio.unc.edu/mcmillan/Comp555S21/reads.fa'
r = requests.get(url, allow_redirects=True)

open('reads.fa', 'wb').write(r.content)
