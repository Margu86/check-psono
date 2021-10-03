# Check_MK healthcheck for psono

## Returncodes
0 ->OK (http request returns 200 and json contains "healthy":true for db_read, db_sync and time_sync)

1 -> WARN (http request returns 200 and json contains "healthy":false for one of the three checks)

2 -> CRIT (http request returns != 200 or json contains "healthy":false for >= two of the three checks)

3 -> UNKNOWN (else)
