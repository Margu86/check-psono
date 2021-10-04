#!/usr/bin/python3

import urllib.request, os, json
from psonosettings import healthurl

try:
    healthcheck = urllib.request.urlopen(healthurl)
    status = healthcheck.read().decode('utf-8')
    if(str(healthcheck.getcode()) == '200'):
        data = json.loads(status)
        healthy = true
        badcount = 0
        badsrvc = ''
        for key, value in data.items():
            if(value != 'true'):
                healthy = false
                badcount += 1
                badsrvc = key
        if(badcount > 0):
            if(badcount > 1):
                print('2 "psono-health" - More than one check returned false')
            else:
                printstr = '1 "psono-health" - {} returned false'.format(badsrvc)
                print(printstr)

    else:
        print('2 "psono-health" - Returncode != 200')
except:
    print('3 "psono-health" - An error ocurred while checking the health')
