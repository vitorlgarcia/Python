# Crie um código em Python que teste se o site YouTube está acessivel pelo computador usado

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')

except:
    print("Deu erro!")

else:
    print("Tudo ok")
    print(site.read()) # Função read() lê todo o arquivo Html do site e o print faz com que o HTML do site seja apresentado na tela.
