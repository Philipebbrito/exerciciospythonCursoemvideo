import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except urllib.error.URLError:
    print('ERRO! Não é possível acessar esse site!!')
else:
    print('TUDO OK!')
    print(site.read())