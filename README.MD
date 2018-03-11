# PyVerge

A Python api client for intracting with the verge block exporer

### Table of content
 
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)


## Installation

 -  Clone repo
 -  python setup.py install
 
 
### Usage
'''python
 
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
