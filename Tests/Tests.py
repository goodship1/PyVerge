import pytest
import requests
import sys
import pyqrcode
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


def test_Get_blockhash_With_non_Genesis():
	index = 12
	url = "https://verge-blockchain.info/api/getblockhash?index=%s"%index
	request_To_verge = requests.get(url,verify = False)
	assert(verge.get_Blockhash(index))== request_To_verge.text

def get_Balance():
	address = "DQkwDpRYUyNNnoEZDf5Cb3QVazh4FuPRs9"
	url ="https://verge-blockchain.info/ext/getbalance/%s"%address
	request_To_verge = requests.get(url,verify = False)
	assert(verge.get_Balance(address)) == request_To_verge.text

def test_Satoshi():
	satoshi_Return_value = verge.satoshi()
	assert(type(satoshi_Return_value))==str

def satoshi_Helper_test():
	satoshi_Return_value = verge._satoshiHelper()
	assert(type(satoshi_Return_value))==tuple
	
def test_Get_moneysupply():
	url = "https://verge-blockchain.info/ext/getmoneysupply"
	request_To_verge = requests.get(url,verify = False)
	assert verge.get_Moneysupply() == request_To_verge.text

def test_get_Diffculty():
	url = "https://verge-blockchain.info/api/getdifficulty"
	request_To_verge = requests.get(url,verify = False)
	assert(verge.get_Difficulty())== request_To_verge.text


def test_transcation_Search():
	number_Transaction = 10
	min_Amount = 10
	url = "https://verge-blockchain.info/ext/getlasttxs/%s/%s"%(number_Transaction,min_Amount)
	request_To_verge = requests.get(url,verify = False)
	assert(verge.transcation_Search(number_Transaction,min_Amount)) == request_To_verge.text


def test_Get_block():
	Hash = "fbb3b1c4da06a043e6b2f45799bda5703c115911f80a58e050423930bc0bfa68"
	url = "https://verge-blockchain.info/api/getblock?hash=%s"%Hash
	request_To_verge = requests.get(url,verify=False)
	assert(verge.get_Block(Hash)) == request_To_verge.text

def test_Get_Distribution():
	url = "https://verge-blockchain.info/ext/getdistribution"
	request_To_verge = requests.get(url,verify=False)
	assert(verge.get_Distribution())== request_To_verge.text


def testing_Negative_index():
	""" Testing of -1 getting block index"""
	index = -1
	url = "https://verge-blockchain.info/api/getblockhash?index=%s"%index
	request_To_verge = requests.get(url,verify = False)
	assert(verge.get_Blockhash(index)) == request_To_verge.text

def testing_Get_qrcode():
	'''testing of get_qrcode with invalid  address'''
	invalid_address = "aaaaaaaa"
	assert(verge.get_Qrcode(invalid_address)) == "cant generate qr code"
	
	
	


def testing_valid_addressqrcode():
	"""check too see if the address is valid on the blockchain"""
	valid_address = "DQkwDpRYUyNNnoEZDf5Cb3QVazh4FuPRs9"
	assert(verge.get_Qrcode(valid_address))!= "cant generate qr code"


