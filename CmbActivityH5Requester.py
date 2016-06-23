import httplib, urllib

addr =  '58.61.30.125:8021'
uri =  '/cmbchina-activity-tran/h5/activity/listActivities4H5'
data = {"param": {"areaCode": "021","channel": 1},"page": 1,"limit": 5}

headers = {"Content-type": "application/json","Accept": "text/plain"}
params = urllib.urlencode(data)
conn = httplib.HTTPConnection(addr)
conn.request("POST", uri, params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()
print data
