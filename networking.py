'''
SSH to multiple devices from a .txt file with the device´s IPs
In this case the script get values for the command show ip interface brief
'''
from netmiko import ConnectHandler
 
with open('devices_IPs.txt') as file_obj:
    for ip in file_obj:
        router = {
            'device_type': 'cisco_ios',
            'ip': ip.strip(),
            'username': 'cisco',  # your username here
            'password': 'cisco',  # your password here
            }

        net_connect = ConnectHandler(**router)

        print (f'##### Device with ip -> {ip} #####')
        print('-' * 80)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print('-' * 80)
 
net_connect.disconnect()
