import pytest
import requests
import sys
sys.path.insert(0,'../PyVerge/')
from pyVerge import PyVerge

verge  = PyVerge()

def test_Blockcount():
	url = "https://verge-blockchain.info/api/getblockcount"
	request_To_verge = requests.get(url,verify = False)
	assert verge.get_Blockcount() == request_To_verge.text

def test_Get_connectioncount():
	url = "https://verge-blockchain.info/api/getconnectioncount"
	request_To_verge = requests.get(url,verify =  False)
	assert verge.get_Connectioncount() ==  request_To_verge.text
	
	
def test_Get_blockhash():
	index = 0#gensis block location
	url = "https://verge-blockchain.info/api/getblockhash?index=%s"%index
	request_To_verge = requests.get(url,verify = False)
	assert verge.get_Blockhash(index) == request_To_verge.text
	
def get_Balance():
	address = "DQkwDpRYUyNNnoEZDf5Cb3QVazh4FuPRs9"
	url ="https://verge-blockchain.info/ext/getbalance/%s"%address
	request_To_verge = requests.get(url,verify = False)
	assert(verge.get_Balance(address)) == request_To_verge.text


def test_Get_top():
	pass

def test_Get_moneysupply():
	url = "https://verge-blockchain.info/ext/getmoneysupply"
	request_To_verge = requests.get(url,verify = False)
	assert verge.get_Moneysupply() == request_To_verge.text

def test_get_Diffculty():
	url = "https://verge-blockchain.info/api/getdifficulty"
	request_To_verge = requests.get(url,verify = False)
	assert(verge.get_Difficulty())== request_To_verge.text
	


def test_Get_wealthdistro():
	pass
	

def test_Get_satoshi():
	pass

def test_Get_movement():
	pass
	

