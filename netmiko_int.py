from netmiko import Netmiko
from netmiko import ConnectHandler

router1 = {'device_type':'cisco_ios','host':'192.168.56.102','username':'cisco','password':'cisco123!','port':22,'secret':'cisco123!','verbose':'True'}

connection = ConnectHandler(**router1)
prompt = connection.find_prompt()
if '>' in prompt:
    connection.enable()

output = connection.send_command('show ip int brief')
print(output)

connection.config_mode()
output = connection.send_command('username cisco secret cisco123!')
connection.exit_config_mode() 
print('Closing connection')
connection.disconnect()
print('#'*40)

router2 = {'device_type':'cisco_ios','host':'192.168.56.104','username':'cisco','password':'cisco123!','port':22,'secret':'cisco123!','verbose':'True'}

connection = ConnectHandler(**router2)
prompt = connection.find_prompt()
if '>' in prompt:
    connection.enable()

output = connection.send_command('show ip int brief')
print(output)

connection.config_mode()
output = connection.send_command('username cisco secret cisco123!')
connection.exit_config_mode() 
print('Closing connection')
connection.disconnect()
print('#'*40)

router3 = {'device_type':'cisco_ios','host':'192.168.56.106','username':'cisco','password':'cisco123!','port':22,'secret':'cisco123!','verbose':'True'}

connection = ConnectHandler(**router3)
prompt = connection.find_prompt()
if '>' in prompt:
    connection.enable()

output = connection.send_command('show ip int brief')
print(output)

connection.config_mode()
output = connection.send_command('username cisco secret cisco123!')
connection.exit_config_mode() 
print('Closing connection')
connection.disconnect()
print('#'*40)