from netmiko import ConnectHandler

# R1 = {
#     'device_type':'cisco-ios',
#     'ip':'192.168.64.100',
#     'port':'22',
#     'username':'admin',
#     'password':'123',
#     'secret':'vnpro'
# }
# connect = ConnectHandler(**R1)

######### KẾT NỐI VỚI ROUTER #########
# connect = ConnectHandler(
#     device_type='cisco_ios',
#     host='192.168.64.100',
#     port=22,
#     username='admin',
#     password='123',
#     secret='vnpro'
# )

######### KẾT NỐI VỚI SWITCH ########
connectSW = ConnectHandler(
    device_type = 'cisco_ios',
    host='192.168.64.163',
    port=22,
    username='admin',
    password='123',
    secret='123'
)

connectSW.enable()
a= connectSW.send_config_set(['vlan 20', 'name Tang 2'])
print(a)

# connect.enable()
# output = connect.send_command('show ip int brief')
# output1 = connect.send_command('show clock')
#output2 = connect.send_config_set('hostname R1_Demo')
# output2 = connect.send_config_set(['int loopback 1','ip add 192.168.2.1 255.255.255.0','no shut'])

# for i in range(2,6):
#     output3 = connect.send_config_set([f'int loopback {i}',f'ip add 192.168.{i+1}.1 255.255.255.0','no shut'])
#     print(output3)

# print(output)