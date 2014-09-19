import urllib3
import json
from Auction import *

def downloadData ():
  url = 'eu.battle.net/api/wow/auction/data/argent-dawn'
  decoded = json.loads(getUrlData(url).decode('utf8'))
  decoded = json.loads(getUrlData(decoded['files'][0]['url']).decode('utf8'))
  print (json.dumps(decoded['alliance']['auctions'],indent=4))
  auctionList = []
  for (i,auction) in enumerate(decoded['horde']['auctions']):
    x = Auction(auction['auc'],auction['item'],auction['owner'],auction['ownerRealm'],auction['bid'],auction['buyout'],auction['quantity'], auction['timeLeft'], auction['rand'], auction['seed'])
    auctionList.append(x)

  return auctionList

def getUrlData (url):
	http = urllib3.PoolManager()
	r = http.request('GET', url)
	return r.data

