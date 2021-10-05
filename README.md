# Check_MK healthcheck for psono

## Usage
1. Clone the recent version to your psono server.
2. Edit the Script and set the URL to yours.
3. Copy the edited Script into the Check_MK folder `cp psono-healthcheck.py /usr/lib/check_mk_agent/local/`
4. Set the execution permission `chmod +x /usr/lib/check_mk_agent/local/psono-healthcheck.py`
5. Got to your Check_MK WATO and search for new services
6. Finished - You should now have a working service named psono-health

## Returncodes
0 ->OK (http request returns 200 and json contains "healthy":true for db_read, db_sync and time_sync)

1 -> WARN (http request returns 200 and json contains "healthy":false for one of the three checks)

2 -> CRIT (http request returns != 200 or json contains "healthy":false for >= two of the three checks)

3 -> UNKNOWN (else)
