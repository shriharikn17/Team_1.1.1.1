# Extension C - Backend Firewall Isolation

## Test setup
- Mac 2: Active nginx edge (10.185.128.147)
- Mac 3: Backend A (10.185.128.163:3001)
- Mac 4: Backend B (10.185.128.32:3002)
- Mac 1: Unauthorized direct-access test client

## Observed results
1. PF rules were enabled on Mac 3 and Mac 4.
2. Mac 2 could connect to both backend ports.
3. Direct connections from Mac 1 timed out.
4. Backend load balancing remained operational.
5. Original /etc/pf.conf files were restored.
6. Project firewall rules were cleared.
7. Both PF activation tokens were released.
8. PF status was verified as Disabled on both Macs.
9. Mac 1 could again connect directly to both backends.

## Configuration files
- configuration/phase2/firewall-backend-a.pf
- configuration/phase2/firewall-backend-b.pf

## Important
These files document the demonstrated rules.
They are not currently active.

The addresses are specific to the demonstration LAN.
