from urllib2 import httplib


class ChileAtiendeClient:
	def __init__(self, token, connection = None):

		self.connection = connection or httplib.HTTPSConnection('www.chileatiende.cl:443')
	def get_servicios(self):
		pass

class Servicio:
	pass
	