# Extension E — DNS-Based Edge Migration

## Original architecture
- Active edge: Mac 2, 10.185.128.147:8443
- Standby edge: Mac 3, 10.185.128.163:8443
- Backend A: Mac 3, port 3001
- Backend B: Mac 4, port 3002
- Primary DNS: Mac 1
- Backup DNS: Mac 4

## Observed migration procedure
1. Configured standby nginx with TLS on Mac 3.
2. Verified its certificate against the project CA.
3. Tested standby HTTPS using curl --resolve.
4. Confirmed both backends returned HTTP 200.
5. Changed app.team1.test to 10.185.128.163
   on both DNS servers.
6. Restarted both DNS services.
7. Verified both DNS servers returned 10.185.128.163.
8. Verified system DNS returned 10.185.128.163.
9. Verified HTTPS returned HTTP 200 via standby nginx 1.31.9.

## Restoration
1. Restored app.team1.test to 10.185.128.147.
2. Restarted both DNS services.
3. Verified HTTPS via original nginx 1.31.6.
4. Removed temporary standby firewall permission.
5. Stopped standby nginx and disabled temporary SSH.

## Evidence
- edge-restored-validation.txt records the healthy state
  after restoring the original edge.

The migration observations above were verified interactively,
not captured as a contemporaneous terminal log.

## Security
TLS private keys are intentionally excluded from GitHub.
The standby configuration remains available for future demos.
