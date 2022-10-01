import nmap
import os
import time
print("""
        __
 _(\    |@@|
(__/\__ \--/ __
   \___|----|  |   __
       \ }{ /\ )_ / _\
       /\__/\ \__O (__
      (--/\--)    \__/
      _)(  )(_
     `---''---` L3DEDE
""")
time.sleep(1)
os.system("clear")
nm = nmap.PortScanner()
host = input("digite la ip: ")
resultado = nm.scan(hosts=host,ports='1-9999',arguments='-sT -Pn ', timeout=10)
print("ip:",host,"nombre:",nm[host].hostname())
print("estado:",nm[host].state())
for proto in nm[host].all_protocols():
    print("protocolo:", proto)
    lport = nm[host][proto].keys()
    sorted(lport)
    for port in lport:
        print("host:", host,"puerto:", port,"estado:",nm[host][proto][port]['state'],"servicios:", nm[host][proto][port]['name'])