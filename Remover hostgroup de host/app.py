from pyzabbix import ZabbixAPI

url = 'https://zabbix-stg.buy4.io/'
username = 'marcos.jesus'
password = 'Mudar123'
zapi = ZabbixAPI(url, timeout=15)

# Iniciando Conexão
try:
    zapi.login(username, password)
    print(f"Conectado com Sucesso! Api-Zabbix, versão atual {zapi.api_version()} \n")
except Exception as err:
    print(f"Falha ao conectar na API do zabbix, Verifique: {err} \n")

#abre o arquivo csv
csvfile = open(r'stagehosts.csv')
hosts = csvfile.readlines()
groups_without_commonalerts = []

for host in hosts:
    host = host.replace('\n', '')

    hostinfo=zapi.host.get(output=['host'],
                  selectGroups='groupid', 
                  filter={'host': host})

    hostid = hostinfo[0]['hostid']
    allgroups = hostinfo[0]['groups']
    allgroups.remove({'groupid': '34'})
    hostupdate = zapi.host.update(hostid=hostid, groups=allgroups)
    print(hostupdate)