import unittest
from urllib2 import httplib

from chileatiende import ChileAtiendeClient, Servicio
from mock import Mock 

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

	def test_custom_connection(self):
		connection = Mock()
		
		client = ChileAtiendeClient(token = self.token, connection = connection)

		self.assertEqual(connection, client.connection)

	@unittest.skip("No hay tiempo")
	def test_get_servicio_object(self):
		client = ChileAtiendeClient(token = self.token)
		
		services = client.get_servicios()
		
		self.assertEqual([Servicio()], services)	

class ServicioTest(unittest.TestCase):

	def test_init(self):
		servicio = Servicio()

		self.assertIsInstance(servicio,Servicio)

if __name__ == '__main__':
    unittest.main()