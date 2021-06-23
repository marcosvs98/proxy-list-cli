with ProxyListClient() as client:
	while True:
		try:
			print(client)
			time.sleep(1)
		except KeyboardInterrupt:
			log.warning('CTRL+C Detected!')

#info = client.get_proxy_info()  self
#print(info.num_proxies)
#print(client.get_proxies())
