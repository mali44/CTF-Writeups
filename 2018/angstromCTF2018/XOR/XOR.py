cipher = 'fbf9eefce1f2f5eaffc5e3f5efc5efe9fffec5fbc5e9f9e8f3eaeee7'.decode('hex')

for i in range(0x00,0xff):
	result = ''
	for j in cipher:
		result += chr(i^ord(j))
	if 'actf{' in result:
		print 'flag :', result
