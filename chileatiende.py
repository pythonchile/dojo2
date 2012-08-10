from urllib2 import httplib


class ChileAtiendeClient:
	def __init__(self, token):
		self.connection = httplib.HTTPSConnection('www.chileatiende.cl:443')