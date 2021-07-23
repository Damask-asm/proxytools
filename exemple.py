from proxytools import *

proxyList = get_free_proxies()

for currentProxy in proxyList:
    if not (is_bad_proxy(currentProxy)):
        print("%s is working" % (currentProxy))
        