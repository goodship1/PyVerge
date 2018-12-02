from setuptools import setup

setup(
	  name = 'pyVerge',
	  version = '1.2',
	  description ='libary to interact with verge blockchain',
	  author ='gavin goodship',
	  packages=['PyVerge'],
	  install_requires=["requests","pyqrcode","bs4"]
	  )
