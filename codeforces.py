import json
from urllib2 import Request, urlopen, URLError

l1=[]
l2=[]
user_handle=raw_input("Type your handle\n")
handle=raw_input("Type other user's handle\n")
request = Request('http://codeforces.com/api/user.status?handle='+handle)
response = urlopen(request)
json_file = response.read()
parsed_json = json.loads(json_file)
for i in parsed_json['result']:
	if i['verdict']=='OK':
		l1.append(str(i['problem']['contestId'])+'-'+str(i['problem']['index']))

request = Request('http://codeforces.com/api/user.status?handle='+user_handle)
response = urlopen(request)
json_file = response.read()
parsed_json = json.loads(json_file)
for i in parsed_json['result']:
	if i['verdict']=='OK':
		l2.append(str(i['problem']['contestId'])+'-'+str(i['problem']['index']))

for a in l1:
	if a not in l2:
		print str(a)





