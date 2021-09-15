# SSH to multiple devices from a .txt file with the device´s IPs
from netmiko import ConnectHandler
 
with open('devices_IPs.txt') as file:
    for ip in file:
        router = {
            'device_type': 'cisco_ios',
            'ip': ip.strip(),
            'username': 'cisco',
            'password': 'cisco',
            }

        net_connect = ConnectHandler(**router)

        print (f'##### Device with ip -> {ip} #####')
        print('-' * 80)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print('-' * 80)
 
net_connect.disconnect()