# Check_MK healthcheck for psono

## Usage
### PSONO-Health
1. Clone the recent version to your psono server into the folder (/usr/lib/check_mk/local/)
2. Edit the Script and set the URL to yours.
3. Set the execution permission `chmod +x /usr/lib/check_mk_agent/local/check-psono/psono-healthcheck.py`
4. Create symbolic link to the python file `ln -s /usr/lib/check_mk/local/check-psono/psono-healthcheck.py /usr/lib/check_mk/local/psono-healthcheck.py`
6. Go to your Check_MK WATO and search for new services
7. Finished - You should now have a working service named psono-health

### Docker Checks
To also Check the Docker Containers you need pip and the docker-py library installed.
If you got that you can uncomment the Lines 4,5,7,9 and 10.
Make shure the Containers you want to check are in the CONTAINER_NAMES list, remove if you don't have all of them on your server.
Also male shure you synchronised the Submodule (`git submodule update --init --recursive`).

## Returncodes
0 ->OK (http request returns 200 and json contains "healthy":true for db_read, db_sync and time_sync)

1 -> WARN (http request returns 200 and json contains "healthy":false for one of the three checks)

2 -> CRIT (http request returns != 200 or json contains "healthy":false for >= two of the three checks)

3 -> UNKNOWN (else)
