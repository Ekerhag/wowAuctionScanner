import urllib3
import json
import os.path
import mysql.connector
from Auction import *

def downloadData ():
  url = 'eu.battle.net/api/wow/auction/data/argent-dawn'
  decoded = json.loads(getUrlData(url).decode('utf8'))
  decoded = json.loads(getUrlData(decoded['files'][0]['url']).decode('utf8'))
#  print (json.dumps(decoded['alliance']['auctions'],indent=4))
  auctionList = []
  for (i,auction) in enumerate(decoded['horde']['auctions']):
    x = Auction(auction['auc'],auction['item'],auction['owner'],auction['ownerRealm'],auction['bid'],auction['buyout'],auction['quantity'], auction['timeLeft'], auction['rand'], auction['seed'])
    auctionList.append(x)

  return auctionList

def downloadItemData (itemId):
	url='eu.battle.net/api/wow/item/' + str(itemId)
	decoded = json.loads(getUrlData(url).decode('utf8'))
	x = Item(decoded['id'],decoded['name'],decoded['sellPrice'])
	return x
	
def getUrlData (url):
	http = urllib3.PoolManager()
	r = http.request('GET', url)
	return r.data

def readItemData():
	filename = 'ItemDatabase.txt'
	f = open(filename, 'r')
	

def writeItemData(itemObject):
	filename = 'ItemDatabase.txt'	
	f = open (filename, 'a')
	f.write(str(itemObject.idNumber) + "," + itemObject.name + "," + str(itemObject.sellPrice) + "\n")

def readItemName(idNumber):
	cnx = mysql.connector.connect(host="localhost", user="root", password="", database="auction")
	cursor = cnx.cursor()
	query = ("SELECT itemName FROM itemData WHERE itemID =" + str(idNumber))
	cursor.execute(query)
	item = cursor.fetchone()
	if (item):
		return item[0]
	else:
		return False
	cursor.close()
	cnx.close()

def writeItemToDatabase(item):
	cnx = mysql.connector.connect(host="localhost", user="root", password="", database="auction")
	cursor = cnx.cursor()
	add_item = ("INSERT INTO itemData "
							"(itemID, itemName, itemSellPrice)"
							"VALUES (%s, %s, %s)")
	item_data = (item.idNumber, item.name, item.sellPrice)
	cursor.execute(add_item, item_data)
	cnx.commit()
	cursor.close()
	cnx.close()

#def writeAuctionToDatabase(auction):

