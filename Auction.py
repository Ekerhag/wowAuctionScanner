#!/home/eekerob/Python-3.4.1/bin/python3.4

class Auction:

	def __init__(self, auc, item, owner, ownerRealm, bid, buyout, quantity, timeLeft, rand, seed):
		self.auc = auc
		self.item = item
		self.owner = owner
		self.ownerRealm	= ownerRealm
		self.bid = bid
		self.buyout = buyout
		self.quantity = quantity
		self.timeLeft = timeLeft
		self.rand = rand
		self.seed = seed

class Item:

	def __init__(self, idNumber, name, sellPrice):
		self.idNumber = idNumber
		self.name = name
		self.sellPrice = sellPrice

