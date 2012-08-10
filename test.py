import unittest
from urllib2 import httplib

from chileatiende import ChileAtiendeClient


class ClientTest(unittest.TestCase):

	token = u'6IWK1x6eVxlAHqRo'

	def test_init(self):
		client = ChileAtiendeClient(token = self.token)

		self.assertIsInstance(client, ChileAtiendeClient)

	def test_connection(self):
		client = ChileAtiendeClient(token = self.token)

		self.assertIsInstance(client.connection, httplib.HTTPSConnection)
		self.assertEqual('www.chileatiende.cl', client.connection.host)
		self.assertEqual(443, client.connection.port)

if __name__ == '__main__':
    unittest.main()