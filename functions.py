import urllib3
import json

def getUrlData (url):
	http = urllib3.PoolManager()
	r = http.request('GET', url)
	return r.data


