#!/usr/bin/python3

import urllib.request, os, json
#from cmk_container_running import containercheck

#CONTAINER_NAMES = ['psono-server', 'psono-client', 'psono-admin-client']


def is_running(container_name):
    container = DOCKER_CLIENT.containers.get(container_name)
    container_state = container.attrs['State']
    container_is_running = container_state['Status'] == RUNNING
    return container_is_running

#for container in CONTAINER_NAMES:
    #cmk_message(container)

try:
    healthcheck = urllib.request.urlopen("https://sub.dom.tld/server/healthcheck/")
    status = healthcheck.read().decode('utf-8')
    if(str(healthcheck.getcode()) == '200'):
        data = json.loads(status)
        badcount = 0
        badsrvc = ''
        if not data["db_read"]["healthy"] :
            print("db_read not healthy")
            badsrvc += "db_read"
            badcount += 1
        if not data["db_sync"]["healthy"] :
            print("db_sync not healthy")
            if(badcount > 0):
                badsrvc += ", db_sync"
            else:
                badsrvc += "db_sync"
            badcount += 1
        if not data["time_sync"]["healthy"] :
            print("time_sync not healthy")
            if(badcount > 0):
                badsrvc += ", time_sync"
            else:
                badsrvc += "time_sync"
            badcount += 1
        if(badcount > 0):
            if(badcount > 1):
                printstr = '2 "psono-health" - {} returned false'.format(badsrvc)
            else:
                printstr = '1 "psono-health" - {} returned false'.format(badsrvc)
            print(printstr)
        else:
            print('0 "psono-health" - all checks passed')
    else:
        print('2 "psono-health" - Returncode != 200')
except:
    print('3 "psono-health" - An error ocurred while checking the health')
