# PyVerge

A Python api client for intracting with the Verge block exporer

### Table of content
 
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Documentation](#documentation)
* [Contribution](#contribution)


## Installation

 -  Clone repo
 -  python setup.py install
 


## Dependencies
-  Requests
-  pyqrcode
-  If dependencies not installed run dependencies.sh



 
### Usage
``` python
 
from PyVerge import PyVerge

verge = PyVerge()

print(verge.get_Difficulty())

{
  "proof-of-work": 51471.70202057,
  "proof-of-work-next": 74007.92238899,
  "proof-of-work-last-height": 1945220,
  "proof-of-stake": 0.00024414,
  "proof-of-stake-next": 74007.92238899,
  "proof-of-stake-last-height": 0,
  "search-interval": 0
}


address = "DQkwDpRYUyNNnoEZDf5Cb3QVazh4FuPRs9"

print(verge.get_Balance(address))
2725553425.7179003


print(verge.get_Moneysupply())
14695794120.548811

Hash = "4181cb8e4274838c651efa85a46247a69c7ed91974e0d9808379656a262a033c"


print(verge.get_Block(Hash))

 "hash": "4181cb8e4274838c651efa85a46247a69c7ed91974e0d9808379656a262a033c",
  "confirmations": 16,
  "size": 1836,
  "height": 1945290,
  "version": 8196,
  "algo_id": 3,
  "algo": "blake",
  "mined_hash": "00000000000002395104afd0f58d74d454bf996a4892ae66fb32574d3518912c",
  "merkleroot": "aeda87b1e4ca186af37b363545072d46b2cd6cf2f590d6a31f7279d55b1fa238",
  "mint": 1560.4,
  "time": 1520782042,
  "nonce": 10680797,
  "bits": "1a02640a",
  "difficulty": 7017365.43163861,
  "previousblockhash": "073c00561b720f6a46d9eb8701297ee7c366a3286045bf8711eca7d55f11d7f4",
  "nextblockhash": "5566330a2eb9e51fd26a3558bc254629c6d813edd6d4d344ef3f0e600b55216f",
  "flags": "proof-of-work",
  "proofhash": "4181cb8e4274838c651efa85a46247a69c7ed91974e0d9808379656a262a033c",
  "entropybit": 0,
  "modifier": "e94c940a51a237d4",
  "modifierchecksum": "5e5dab2c",
  "tx": [
    "58f1beff9dee6d4b59b365ae7e370ba55127a817b7542281895b4d7ccdf00a1e",
    "bb24b287c991ac788af623a7ba350729e4c0e0a7145c58abea8f7d2c5e6f6889",
    "a1aac77256e68fe315824323ea640aa3758f2ccbb0302855e926722c97e5ce83",
    "925700f96fff0f8db2d64484eab001cec4ce0eb0cfd423c039d26dd38665c132",
    "42dcd327773e1ffbef7ad0ed66009ca753104e3555cdc236c0967bf744508d62"
  ],
  "signature": "3044022034dc7ff97611880772bd16dfb2b8745e6dffb47f4e274ebe14d531105245f3b102200b267c8f034672b2ae84ce5e38ae2a7d26930c5572f4575c266faa55808e3afb"
}
```
### Features
  - Get balance from address
  - Get money supply
  - Get hash information
  -Gets qrcode from public address
  
### Documentation
  - [click](https://github.com/goodship1/PyVerge/wiki/Documentation)
  
  
  
### Contribution 
 - Feel to create a pull request 
 
 
