
import os 
class BaseConfig(object):
	DEBUG=False 
	SECRET_KEY='g\xe2H\t\x06\xfe\xf1w\xb2v&\xac\x0b0\r\xd2\xa5\x19\x86\xd2\xc8k\x1b\x17\xdd'
	
	'''
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	#set DATABASE_URL='sqlite:///po.db'

	'''
	SQLALCHEMY_DATABASE_URI = 'sqlite:///po.db'
	
	


class DevelopementConfig(BaseConfig):
	DEBUG = True
	

class ProductionConfig(BaseConfig):
	DEBUG = False