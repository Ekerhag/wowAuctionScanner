#!/home/eekerob/Python-3.4.1/bin/python3.4
import json
from functions import *
from Auction import *

# Variables
url = 'eu.battle.net/api/wow/auction/data/argent-dawn'

## Method
decoded = json.loads(getUrlData(url).decode('utf8')) ##decode to utf8

#print (json.dumps(decoded, indent=4))

#print (decoded['files'][0]['url'])
#print (decoded['files'][0]['lastModified'])

decoded = json.loads(getUrlData(decoded['files'][0]['url']).decode('utf8'))

print (json.dumps(decoded['alliance']['auctions'],indent=4))
auctionList = []
for (i,auction) in enumerate(decoded['horde']['auctions']):
	x = Auction(auction['auc'],auction['item'],auction['owner'],auction['ownerRealm'],auction['bid'],auction['buyout'],auction['quantity'], auction['timeLeft'], auction['rand'], auction['seed'])
	auctionList.append(x)

print (getattr(auctionList[0], 'auc'))
