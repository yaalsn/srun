__author__="asn"
import uuid
from binascii import b2a_hex
import struct
import socket
from time import sleep

CONF = "srun.conf"

def get_mac_address(): 
	mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
	return ":".join([mac[e:e+2] for e in range(0,11,2)])
	
def get_foo_package(username):
	username_hex = b2a_hex(username)
	mac_hex = b2a_hex(get_mac_address())
	length = len(username_hex)/2
	foo_32 = username_hex + (32 - length) * '00'
	foo_17 = mac_hex
	foo_7 = '00' * 7
	foo_56 = foo_32 + foo_17 + foo_7
	return foo_56

def get_package(foo_56):
	str_foo = get_foo_package(username)
	str1 = ''
	package = ''
	while str_foo:
		str1 = str_foo[0:2]
		s = int( str1, 16)
		package += struct.pack('B', s)
		str_foo = str_foo[2:]
	return package

def send_package(package):
	addr = (server, 3338)
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while(1):
		client.sendto(package, addr)
		sleep(50)

if __name__ == '__main__':
	execfile(CONF, globals())
	send_package(get_package(get_foo_package(username)))
