CONF = "./etc/srun.conf"
#'{SRUN3}\r\n' + 'ascii+4'
def get_username(username):
	fuck_username = '{SRUN3}\\r\\n'
	for i in username:
		j = chr(ord(i) + 4)
		fuck_username = fuck_username + j
	return fuck_username

if __name__ == '__main__':
	execfile(CONF, globals())
	with open('fuck.txt','w') as f:
		f.write(get_username(username))
