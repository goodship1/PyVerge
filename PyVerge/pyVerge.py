import requests
import urllib3
import BeautifulSoup
urllib3.disable_warnings()


class PyVerge(object):
	
	
	def __init__(self):
		self.transcation_count = 0
		self.transaction = {}
	
	def __str__(self):
		return "pyverge is a python libary which instracts with verge blockchain"
	
	def __iter__(self):
		return self
	
	def next(self):
		pass
	
	def __gt__(self,other):
		pass
	
	def __eq__(self,other):
		pass
	
	def get_Difficulty(self):
		url = "https://verge-blockchain.info/api/getdifficulty"
		request_To_verge = requests.get(url ,verify = False)
		return request_To_verge.text
	
	def get_Connectioncount(self):
		url = "https://verge-blockchain.info/api/getconnectioncount"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	
	def get_Blockcount(self):
		url  = "https://verge-blockchain.info/api/getblockcount"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	def get_Blockhash(self,index=0):
		"""gets the block hash at index value
		if no value provided gets the gensis block by default"""
		url = "https://verge-blockchain.info/api/getblockhash?index=%s"%index
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	def _get_Satoshi_helper(self):
		url = "https://verge-blockchain.info/"
		request_To_verge = requests.get(url)
		pass
	
	def _get_Top_helper(self):
		"""get_top helper to scrap verge website"""
		pass
	
	
	def get_Satoshi(self):
		"""Returns the satoshi value of Verge Coin"""
		pass
	

	
	def get_Moneysupply(self):
		url = "https://verge-blockchain.info/ext/getmoneysupply"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	def transcation_search(self,min_amount,number_Transcation):
		pass
	
	def get_Balance(self,address):
		url = "https://verge-blockchain.info/ext/getbalance/%s"%address
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
		
	
	
	def get_Wealthdistro(self):
		pass
	
	def get_Movement(self,date):
		pass

