"""*********************************************************************
*                                                                      *
*            Description: Implementing a python client for proxy list  *
*                         Date:  12/05/2021                            *
*                 Author: Marcos Vinicios da Silveira                  *
*                                                                      *
************************************************************************
"""
import time
import unittest
from proxy_list import ProxyListClient

class ProxyListClientTester(unittest.TestCase):

	def test_service(self):
		count = 0
		with ProxyListClient() as client:
			while True:
				try:
					print(client)
					time.sleep(1)
					count += 1
				except KeyboardInterrupt:
					log.warning('CTRL+C Detected!')
				try:
					self.assertEqual(count, 1)
					break
				except AssertionError as e:
					continue

	def test_get_proxies(self):
		client = ProxyListClient()
		self.assertTrue(client.get_proxies())

	def test_proxies_filter_http(self):
		client = ProxyListClient()
		self.assertTrue(client.get_proxies('scheme.http'))

	def test_proxies_filter_https(self):
		client = ProxyListClient()
		self.assertTrue(client.get_proxies('scheme.https'))

	def test_proxies_filter_level_anonymity(self):
		client = ProxyListClient()
		self.assertTrue(client.get_proxies('level_anonymity.0'))

	def test_proxies_filter_country(self):
		client = ProxyListClient()
		self.assertTrue(client.get_proxies('country.US'))

	def test_proxies_filter_http_port(self):
		client = ProxyListClient()
		self.assertTrue(client.get_proxies('http-port.8080'))


if __name__ == '__main__':
    unittest.main()

# end-of-file