import requests
import urllib3
urllib3.disable_warnings()


class PyVerge(object):
	
	def get_Connectioncount(self):
		url = "https://verge-blockchain.info/api/getconnectioncount"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	def get_Blockcount(self):
		url  = " https://verge-blockchain.info/api/getconnectioncount"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text
	
	def get_Blockindex(self,index):
		pass
	
	def get_Block(self):
		pass
	
	def get_Top(self,top_accounts):
		pass
	
	def get_Moneysupply(self):
		pass
	
	def get_Wealthdistro(self):
		pass
	

c = PyVerge()
print(c.get_Blockcount())
