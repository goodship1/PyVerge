from __future__ import division
import ast
import requests
import urllib3
import pyqrcode
from pyvergeexceptions import QrcodeGenerationError
urllib3.disable_warnings()


class PyVerge(object):



	def __str__(self):
		return "PyVerge is a python libary which instracts with verge blockchain"


	def get_difficulty(self):
		url = "https://verge-blockchain.info/api/getdifficulty"
		request_To_verge = requests.get(url ,verify = False)
		return request_To_verge.text

	def get_connectioncount(self):
		url = "https://verge-blockchain.info/api/getconnectioncount"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text


	def get_blockcount(self):
		url  = "https://verge-blockchain.info/api/getblockcount"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text

	def get_block(self,Hash):
		url = "https://verge-blockchain.info/api/getblock?hash=%s"%Hash
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text

	def get_blockhash(self,index=0):
		"""gets the block hash at index value
		if no value provided gets the gensis block by default"""
		url = "https://verge-blockchain.info/api/getblockhash?index=%s"%index
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text


	def get_satoshi(self):
		satoshi_Calulation = self._satoshiHelper()
		btc = satoshi_Calulation[0]
		verge = satoshi_Calulation[1]
		return format(verge/btc,'.10f')
	
		 
		 
	def _satoshiHelper(self):
		btc_Price_url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%("BTC","USD")
		verge_Price_url ="https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%("XVG","USD")
		request_Btc_price = requests.get(btc_Price_url)
		request_Verge_price = requests.get(verge_Price_url)
		return self._satoshiUnicodeformatting(request_Btc_price.text,request_Verge_price.text)
		
		
	
	def _satoshiUnicodeformatting(self,btc_Request,Verge_Request):
		price = "USD"
		btc = ast.literal_eval(btc_Request)
		verge = ast.literal_eval(Verge_Request)
		return (btc[price],verge[price])
	
	def get_Moneysupply(self):
		url = "https://verge-blockchain.info/ext/getmoneysupply"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text

	def transcation_Search(self,min_amount,number_Transcation):
		url = "https://verge-blockchain.info/ext/getlasttxs/%s/%s"%(number_Transcation,min_amount)
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text

	def get_balance(self,address):
		url = "https://verge-blockchain.info/ext/getbalance/%s"%address
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text



	def get_distribution(self):
		url = "https://verge-blockchain.info/ext/getdistribution"
		request_To_verge = requests.get(url,verify = False)
		return request_To_verge.text


	def mail_Qrcode(self):
		pass
		#function to send qrcode to email address

	def get_Qrcode(self,address ,qr_Size=None):
		try:
			check = float(self.get_Balance(address))
		except Exception as err:
			raise QrcodeGenerationError("cant generate qr code")
		if(qr_Size!=None):
			wallet=pyqrcode.create(address,size=qr_Size)
			wallet_To_terminal = wallet.terminal()
			print(wallet_To_terminal)
		else:
			wallet=pyqrcode.create(address)
			wallet_To_terminal = wallet.terminal()
			print(wallet_To_terminal)
