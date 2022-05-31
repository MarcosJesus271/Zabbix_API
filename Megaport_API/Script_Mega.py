from pyzabbix import ZabbixAPI
from datetime import datetime, timezone
import time

#! Conectar Zabbix-STG
zapi = ZabbixAPI("*********************")

try:
    zapi.login(user="Admin", password="zabbix")
    print(f"\nConectado ao Zabbix-STG, versão {zapi.api_version()} \n")
except Exception as err:
    print(F"\nErro ao conectar, verifique: {err} \n")

#! Definidor de milisegundos
# Pegue meu horario e converta para o epoch (ok),
# Pegue 5 minutos atrás do meu epoch coletado (ok), 
# Armazene em variavel e aguarde mais 5 minutos (),
# Repita o processo. 
tempo = '23456789098765432'
for i in tempo:
    try:
        epoch = datetime.now()
        d = epoch.isoformat()
        dt = datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%f')
        dt = dt.replace(tzinfo=timezone.utc)
        seconds_since_epoch = dt.timestamp()
        epoch = str(seconds_since_epoch)
        epoch_value = epoch.replace(".","")
        print("Horario atual:", epoch_value)

        conta = (seconds_since_epoch)
        conta = str(conta)
        conta = conta.replace(".", "")
        epoch_value5m = int(conta)
        epoc2 = (epoch_value5m - 300000000)
        print("5 minutos anteriores:", epoc2)
       

    
        #! Busca o ID do template
        host_gest = zapi.template.get(output = "extend",
                                        filter = {"host": ["Template Status MegaPort NEW"]})
        templateid = host_gest
        dicthost = templateid[0]['templateid']      
        #! Buscar IDs dos templates
        item_get = zapi.item.get(output = ["itemid","query_fields","\n"],
                                hostids = str(dicthost))        
        for i in range(0,40):
            dicionary = item_get[i]
            dictionary = {'itemid': dicionary['itemid']}
            lista_id = dictionary.items()
            for a,b in lista_id:
                ids = b
                print(ids + ' Atualizado com sucesso')
            #! Atualiza os itens do template
                item_update = zapi.item.update({
                                "itemid": str(ids),
                                "query_fields": [{"type": "A_BITS"},
                                                {"from": str(epoch_value)},
                                                {"to":str(epoc2)}]
                                                                                })
        print("\nConcluido\n")
        print("Aguardando 5 minutos...")
        time.sleep(60)     
        print("Aguardando 4 minutos...") 
        time.sleep(60)    
        print("Aguardando 3 minutos...") 
        time.sleep(60)    
        print("Aguardando 2 minutos...")  
        time.sleep(60)   
        print("Aguardando 1 minutos...")
        print("\n=-=-==-=-=-=-=-=-=-=\n")    

                                                               
    except:
        print("\nSistema desligado\n")
