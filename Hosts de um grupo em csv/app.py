from zabbix_api import ZabbixAPI
from pyzabbix import ZabbixAPI
import dotenv, os, time, csv

dotenv.load_dotenv(dotenv.find_dotenv())
url = os.getenv("url")
username = os.getenv("username")
password = os.getenv("password")
zapi = ZabbixAPI(url, timeout=15)

# Iniciando Conexão
try:
    zapi.login(username, password)
    print(f"Conectado com Sucesso! Api-Zabbix, versão atual {zapi.api_version()} \n")
except Exception as err:
    print(f"Falha ao conectar na API do zabbix, Verifique: {err} \n")


##bloco de pesquisa 25-41
hostgroupgetid = zapi.hostgroup.get(output='extend', 
                                    selectHosts='hostids', 
                                    filter={'name':['algum_hostgroup']}) 

#Itera a cada host id e busca o host name daquele host id
c = 0

with open('Save_hosts.csv','a') as csvfile:
          writer = csv.writer(csvfile, delimiter=',')
          line = ["Hostnames", "Groups"]
          writer.writerow(line)

for id in hostgroupgetid[0]['hosts']:
    c += 1
    host_id = id['hostid']
    infohost = zapi.host.get(output=['host'],
                                    selectGroups='extend', 
                                    filter={'hostid': host_id})
    
    hostname = (infohost[0]['host'])
    hostgroups = (infohost[0]['groups'])
    
    print(hostname)

    with open('Save_hosts.csv','a') as csvfile:
           writer = csv.writer(csvfile, delimiter=',')
           line = [hostname]
           writer.writerow('\n')
           writer.writerow(line)   

    for groups in hostgroups:
        with open('Save_hosts.csv','a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                line = [str(" "), groups['name']]
                writer.writerow(line)

    print(groups['name'])
    
    if c == 20:
        time.sleep(3)
        c = 0


print("Impressão concluida")
    