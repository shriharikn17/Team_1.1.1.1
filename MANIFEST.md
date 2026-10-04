# Team 1.1.1.1 Submission Manifest

## Core documentation
- `README.md`
- `architecture/ip_table.md`
- `architecture/network_topology.md`
- `architecture/request_flow.md`
- `architecture/dhcp_notes.md`

## Configuration
- `configuration/dnsmasq.conf`
- `configuration/backend.conf`
- `configuration/TLS-notes.md`
- `configuration/backend-launch-instructions.md`

## Backend source
- `backends/backend-a/server.py`
- `backends/backend-b/server.py`
- `_submission_/Backend-Source-Code.zip`

## Evidence
- `evidence/01-lan/` — LAN addressing and reachability
- `evidence/02-dns/` — private DNS and public forwarding
- `evidence/03-backends/` — direct backend tests
- `evidence/04-https-tls/` — trusted HTTPS and TLS
- `evidence/05-load-balancing/` — Backend A/B distribution
- `evidence/06-http-cache/` — ETag / 304 validation
- `evidence/07-wireshark/` — DNS, TCP, TLS and HTTP packet analysis
- `evidence/08-failure-tests/` — five failure scenarios with screenshots

## Capture
- `captures/mac4_capture.pcapng`

## Security note
The TLS private key is intentionally not included in this repository/package.
