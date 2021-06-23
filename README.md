# proxy-list-pycli
Responsible for implementing, filtering and manipulating public proxy lists obtained from 'https://github.com/clarketm/proxy-list'

#### Cliente

```pycon
>>> from proxy_list import ProxyListClient
>>> 
>>> client = ProxyListClient()
>>> client.client.get_proxies('scheme.https')[0:1]
[ProxyParsed(proxy_host='38.21.36.136', proxy_port='8080', proxy_scheme='https', proxy_level_anonymity=0, proxy_country='US', proxy_google_passed=False, proxy_outgoing_ip=False, proxy_uri='https://38.21.36.136:8080/', proxy_user=None, proxy_pass=None, proxy_status='no-status-available')]
>>>
>>> client.get_proxy_info.num_proxies
400
>>>
```

##### Proxy List Cache
```
{
    "info": {
        "header": [
            "Proxy list (#400) updated at Tue, 22 Jun 21 07:55:01 +0300",
            "Mirrors=https://spys.me/proxy.txt https://t.me/spys_one",
            "Support by donations:",
            "BTC 1H1ZH7WJVzU7GMDSwsAQrqvGrbLY49wdae",
            "ETC 0xd1Cf57E35003aD846524a7778D99e8856B96C241",
            "BCH 19o72EjQw3mEYNciZ4JxvpDmUbjjtXghBb",
            "LTC LMrLZNWGYK3kMHvyioBqZdXYWE3pKj7xZX",
            "IP address:Port CountryCode-Anonymity(Noa/Anm/Hia)-SSL_support(S)-Google_passed(+)"
        ],
        "updated": "2021-06-22 22:29:36.179899",
        "num_proxies": 400,
        "success": 31,
        "failure": 21,
        "no-status-available": 348,
        "success-rate": "61.75%",
        "failure-rate": "38.25%"
    },
    "status": {...},
    "scheme": {...},
    "level_anonymity": {...},
    "country": {...},
    "http-port": {...},
    "google_passed": {...},
    "raw": [
        {
            "proxy_host": "62.171.167.17",
            "proxy_port": "3128",
            "proxy_scheme": "http",
            "proxy_level_anonymity": 0,
            "proxy_country": "DE",
            "proxy_google_passed": false,
            "proxy_outgoing_ip": false,
            "proxy_uri": "http://62.171.167.17:3128/",
            "proxy_user": null,
            "proxy_pass": null,
            "proxy_status": "no-status-available"
        }
    .....
    ]    
```
