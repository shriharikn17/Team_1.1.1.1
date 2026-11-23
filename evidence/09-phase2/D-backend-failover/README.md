# Extension D — Backend High Availability

## Architecture
- nginx active edge: Mac 2, port 8443
- Backend A: Mac 3, port 3001
- Backend B: Mac 4, port 3002

## Previously observed failure experiment
1. Both backends were running and serving requests.
2. Backend A was deliberately stopped.
3. Ten HTTPS requests returned HTTP 200 from Backend B.
4. Backend A was restarted.
5. Subsequent requests returned HTTP 200 from both A and B.

## Recovery evidence
See backend-ha-validation.txt for the current healthy
load-balancing test.

## Conclusion
nginx continued serving requests through Backend B during
Backend A's simulated outage.

The earlier outage observations were verified interactively;
this file is a summary, not a contemporaneous outage log.
