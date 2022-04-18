from pyzabbix import ZabbixAPI
import csv, os

url = 'Url_local'
username = 'Algum_usuario'
password = 'Algum_password'
zapi = ZabbixAPI(url, timeout=15)

def connection():
    try:
        zapi.login(username, password)
        print(zapi.api_version())
        print(f'Conectado com Sucesso! APi-ZABBIX, versão atual {zapi.api_version()}')
    except Exception as err:
        print(f'Falha ao conectar na API do zabbix, Verifique: {err}')

groupids = ['37', '21','38','39']
groups = [{"groupid": groupid} for groupid in groupids]
print(groups)

info_interfaces = {
    "1": {"type": "agent", "id": "1", "port": "10050"},
    "2": {"type": "SNMP", "id": "2", "port": "161"},
}

def create_host(pos1, pos2):
        zapi = ZabbixAPI(url, timeout=15)
        zapi.login(username, password)
        try:
            create_host = zapi.host.create({
                "groups": groups,
                "host": str(pos1),
                "interfaces": {
                    "type": info_interfaces['1']['id'],
                    "main": 1,
                    "useip": 1,
                    "ip": str(pos2),
                    "dns": "",
                    "port": info_interfaces['1']['port']
                }
            })
            print(f'Host {pos1} cadastrado com sucesso')
        except Exception as err:
            print(f'Falha a cadastrar o host: Verifique: {err}')

#Faz a tratativa dos dados csv
with open('Passeio_Corporate.csv', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")

    for linha in reader:
        pos1 = linha[0]
        pos2 = linha[1]

        print("Host:",pos1)
        print("Ip:",pos2)
        create_host(pos1, pos2)

        print('\n')

