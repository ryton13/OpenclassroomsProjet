#################################################################################
#       Configuration switch                                                    #
#             Juin 2021                                                         #
#            Henri KAHUDI                                                       #
#################################################################################


import netmiko
from netmiko import ConnectHandler
from time import sleep
import sys

dev = {
    'device_type' : 'cisco_ios',			#déclaration du type de matériel
    'host' : '192.168.0.10',				#adresse ip du matériel
    'username' : 'admin',				#identifiant
    'password' : 'admincisco',				#mot de passe en clair
    'secret' : 'ciscoadmin',				#mot de passe chiffré
    } 							#On utilise un dictionnaire pour l'authentification

switch_conn = ConnectHandler(**dev)			#
switch_conn.enable()					#

print("*****************Connexion établie sur le Switch********************")

print("*****************Configuration initiale********************")
output = switch_conn.send_command("show ip int brief")				#commande pour afficher un résumé de la config des interfaces
print(output)
sleep(5)


print("*****************Configuration des VLANS********************")

config_commands_vlan20 = ['vlan 20', 'name Service Operationnel', 'int G0/2', 'switchport mode access', 'switchport access vlan 20', 'int vlan 20', 'ip address 192.168.1.126 255.255.255.128', 'no shutdown']
output = switch_conn.send_config_set(config_commands_vlan20)
print(output)

config_commands_vlan8 = ['vlan 8', 'name Service Commercial', 'int G0/3', 'switchport mode access', 'switchport access vlan 8', 'int vlan 8', 'ip address 192.168.1.158 255.255.255.224', 'no shutdown']
output = switch_conn.send_config_set(config_commands_vlan8)
print(output)

config_commands_vlan89 = ['vlan 89', 'name Service RH', 'int G1/0', 'switchport mode access', 'switchport access vlan 89', 'int vlan 89', 'ip address 192.168.1.174 255.255.255.240', 'no shutdown']
output = switch_conn.send_config_set(config_commands_vlan89)
print(output)

config_commands_vlan90 = ['vlan 90', 'name Service Comptabilite', 'int G1/1', 'switchport mode access', 'switchport access vlan 90', 'int vlan 90', 'ip address 192.168.1.190 255.255.255.240', 'no shutdown']
output = switch_conn.send_config_set(config_commands_vlan90)
print(output)

config_commands_vlan7 = ['vlan 7', 'name Service Informatique', 'int G1/2', 'switchport mode access', 'switchport access vlan 7', 'int vlan 7', 'ip address 192.168.1.198 255.255.255.248', 'no shutdown']
output = switch_conn.send_config_set(config_commands_vlan7)
print(output)

config_commands_vlan10 = ['vlan 10', 'name Imprimante', 'int G1/3', 'switchport mode access', 'switchport access vlan 10', 'int vlan 10', 'ip address 192.168.1.206 255.255.255.248', 'no shutdown']
output = switch_conn.send_config_set(config_commands_vlan10)
print(output)

config_commands_vlan13 = ['vlan 13', 'name Server', 'int G0/1', 'switchport mode access', 'switchport access vlan 13', 'int vlan 13', 'ip address 192.168.1.214 255.255.255.248', 'no shutdown']
output = switch_conn.send_config_set(config_commands_vlan13)
print(output)
sleep(5)

print("*****************Configuration du serveur dns********************")
config_commands_dns = ['ip domain-lookup', 'ip name-server 192.168.0.2']
output = switch_conn.send_config_set(config_commands_dns)
print(output)

print("*****************Configuration de la route par defaut********************")
config_commands_last_resort = ['ip routing', 'ip route 0.0.0.0 0.0.0.0 192.168.0.2']
output = switch_conn.send_config_set(config_commands_last_resort)
print(output)

print("*****************Configuration des agents relais DHCP********************")
config_commands_vlan20 = ['int vlan 20', 'ip helper-address 192.168.1.209']
output = switch_conn.send_config_set(config_commands_vlan20)
print(output)
config_commands_vlan8 = ['int vlan 8', 'ip helper-address 192.168.1.209']
output = switch_conn.send_config_set(config_commands_vlan8)
print(output)
config_commands_vlan89 = ['int vlan 89', 'ip helper-address 192.168.1.209']
output = switch_conn.send_config_set(config_commands_vlan89)
print(output)
config_commands_vlan90 = ['int vlan 90', 'ip helper-address 192.168.1.209']
output = switch_conn.send_config_set(config_commands_vlan90)
print(output)
config_commands_vlan7 = ['int vlan 7', 'ip helper-address 192.168.1.209']
output = switch_conn.send_config_set(config_commands_vlan7)
print(output)
config_commands_vlan10 = ['int vlan 10', 'ip helper-address 192.168.1.209']
output = switch_conn.send_config_set(config_commands_vlan10)
print(output)



print("*****************Configuration finale********************")
output = switch_conn.send_command("show ip int brief")
print(output)
output = switch_conn.send_command("show ip route")
print(output)
output = switch_conn.send_command("write")
print(output)






