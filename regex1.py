import re

str = '''itd device-group DG1
	node ip 10.2.100.1
	node ip 10.2.100.2
	node ip 10.2.100.3
	node ip 10.2.100.4

itd SER1
	device-group DG1
	ingress-interface vlan 67
	load-balance method src ip buckets 64
	no sh'''
	

'''output = {
'SER1':
	{
	'DG1':
		{
		'node_1' : '10.2.100.1',
		'node_2' : '10.2.100.2',
		'node_3' : '10.2.100.3',
		'node_4' : '10.2.100.4'
		},
	'interface': 'vlan67',
	'load-balance': 'src ip',
	'buckets': '64'
	
	}
}'''

deviceGroup = re.search('device-group\s(.*)\n',str)
deviceGroup = deviceGroup.group(1)

itd = re.search('itd\s(\w+$)',str,re.M)
itd = itd.group(1)

interface = re.search('(interface\s(.*))',str,re.M)
interface = interface.group(2)

loadBalance_buckets = re.search('(load-balance method\s(.*)\sbuckets\s(.*))',str)

loadBalance = loadBalance_buckets.group(2)
bucket = loadBalance_buckets.group(3)

output = dict()

output[itd]={}

nodes=[]
ips = re.findall('node\sip\s(.*)',str)

x=1

for x in range(1,len(ips)+1):
  ele = 'node'+'_{}'.format(x)
  x = x+1
  nodes.append(ele)

dgi = dict(zip(nodes,ips))

ser1 = dict()
ser1[deviceGroup]=dgi
m = ['interface','load-balance','bucket']
n = [interface,loadBalance, bucket]

for x in range(len(m)):
  ser1[m[x]] = n[x]

output[itd]=ser1
print(output)
