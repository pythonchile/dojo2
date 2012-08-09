import unittest
from chileatiende import ChileAtiendeClient

class ClientTest(unittest.TestCase):
	token = u'6IWK1x6eVxlAHqRo'
	def test_init(self):
		client = ChileAtiendeClient(token = self.token)
		
		self.assertIsInstance(client, ChileAtiendeClient)


if __name__ == '__main__':
    unittest.main()