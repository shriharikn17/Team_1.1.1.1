# Phase 2 — Team 1.1.1.1

## Network roles

| Device | Role | LAN IP |
|---|---|---|
| Mac 1 — Saksham | Primary DNS | 10.185.128.177 |
| Mac 2 — Shrihari | Active nginx edge | 10.185.128.147 |
| Mac 3 — Rachit | Backend A / standby edge | 10.185.128.163 |
| Mac 4 — Amogha | Backend B / backup DNS | 10.185.128.32 |

## Implemented extensions

- A: Primary and backup DNS with failover and recovery
- B: 30-second DNS TTL and controlled record-change experiment
- C: PF-based backend isolation and rollback
- D: Backend failover and load balancing
- E: Standby nginx with DNS-based edge migration and restoration
- F: Fault diagnosis and service recovery

## Configuration

See `configuration/phase2/`.

## Evidence

See `evidence/09-phase2/`.

Current validation logs and written accounts of earlier
experiments are distinguished in the evidence files.

## Restored operating state

- Both DNS servers running
- Application DNS points to Mac 2
- Active nginx running on Mac 2, port 8443
- Both backends running
- Standby nginx stopped, configuration retained
- PF disabled on Mac 3 and Mac 4
- Temporary SSH access disabled on Mac 3

## Notes

IP addresses depend on the demonstration LAN.
TLS private keys are not stored in GitHub.
