import requests
import urllib3
urllib3.disable_warnings()


class PyVerge(object):
	
	

	def __str__(self):
		return "pyverge is a python libary which instracts with verge blockchain"
	
	
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
	
	def get_Block(self,Hash):
		url = "https://verge-blockchain.info/api/getblock?hash=%s"%Hash
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	def get_Blockhash(self,index=0):
		"""gets the block hash at index value
		if no value provided gets the gensis block by default"""
		url = "https://verge-blockchain.info/api/getblockhash?index=%s"%index
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	


	
	def get_Moneysupply(self):
		url = "https://verge-blockchain.info/ext/getmoneysupply"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	def transcation_Search(self,min_amount,number_Transcation):
		url = "https://verge-blockchain.info/ext/getlasttxs/%s/%s"%(number_Transcation,min_amount)
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	def get_Balance(self,address):
		url = "https://verge-blockchain.info/ext/getbalance/%s"%address
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
		
	
	
	def get_Distribution(self):
		url = "https://verge-blockchain.info/ext/getdistribution"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	def get_Qrcode():
		pass
	
	
