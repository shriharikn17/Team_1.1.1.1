# Extension F — Fault Diagnosis and Recovery

## Fault 1: nginx edge service stopped

The active nginx service on Mac 2 was deliberately stopped.

### Diagnostic observations from Mac 1
- DNS query to the primary server succeeded.
- Ping to Mac 2 succeeded: 3/3 packets.
- TCP connection to port 8443 was refused.
- HTTPS with curl --resolve also failed.

### Diagnosis
Mac 2 was reachable, but its HTTPS service was stopped.

### Recovery
- Validated nginx configuration using nginx -t.
- Restarted nginx.
- Confirmed port 8443 was listening.

## Fault 2: Incorrect client DNS settings

Mac 1 initially used public DNS server 8.8.8.8.

### Symptoms
- Direct queries to project DNS succeeded.
- System hostname resolution failed.
- curl reported: Could not resolve host.

### Recovery
Configured Mac 1 to use:
1. 127.0.0.1 — local primary DNS
2. 10.185.128.32 — backup DNS

System resolution then returned 10.185.128.147.

## Final verification

After recovery:
- System DNS resolved correctly.
- HTTPS returned HTTP 200.
- Six requests succeeded.
- Both Backend A and Backend B responded.

These diagnostic observations were verified interactively
during the exercise and are summarized here.
