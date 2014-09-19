#!/usr/lib/python3.4
from functions import *
import time
# downloadData()
# readAuctionDataFromFile()
# readItemDataFromFile()
# 

i = 0
auctionList = downloadData()
for auction in auctionList:
	print (auction.item)
	auction.name = readItemName(auction.item)
	if (auction.name):
		print ("Exists in database")
	else:
		print ("Downloading data to database")
		x = downloadItemData(auction.item)
		writeItemToDatabase(x)


