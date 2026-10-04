# Team 1.1.1.1 - Computer Networks Project

## Team Members

- Saksham Narotra — Mac 1 — DNS server (`dnsmasq`)
- Shrihari K.N — Mac 2 — Nginx reverse proxy / load balancer / TLS termination
- Rachit Singh — Mac 3 — Backend A
- Amogha Raj Sandur — Mac 4 — Backend B and test client

## Phase 1 Summary

This project uses the following network setup:

- LAN connectivity across four Macs
- Private DNS for `app.team1.test` and `api.team1.test`
- Public DNS forwarding through `dnsmasq`
- Two Python HTTP backend servers
- Nginx reverse proxying and round-robin load balancing
- HTTPS/TLS termination with the team local CA
- HTTP cache validation using `ETag` / `If-None-Match`
- Wireshark verification of DNS, TCP, TLS and HTTP forwarding
- Failure testing for wrong ports, unavailable backends and DNS faults

## Network Setup

| Machine | Role | IP | Port / Service |
|---|---|---|---|
| Mac 1 | DNS server | `10.7.1.82` | DNS `53` / `dnsmasq` |
| Mac 2 | Nginx reverse proxy / load balancer | `10.7.20.19` | HTTP `8081`, HTTPS `8443` |
| Mac 3 | Backend A | `10.7.13.26` | HTTP `3001` |
| Mac 4 | Backend B | `10.7.1.23` | HTTP `3002` |

Private records:

```text
app.team1.test -> 10.7.20.19
api.team1.test -> 10.7.20.19
```

> The lab WLAN used DHCP, so some screenshots from different sessions show different IP addresses. See [`architecture/dhcp_notes.md`](architecture/dhcp_notes.md) for the address changes.

## Request Flow

```text
Client
  |
  | 1. DNS query: app.team1.test
  v
Mac 1 / dnsmasq
  |
  | 2. A record -> Nginx IP
  v
Mac 2 / Nginx :8443
  |
  | 3. TLS termination + reverse proxy
  | 4. round-robin upstream selection
  +---------------------------+
  |                           |
  v                           v
Mac 3 / Backend A          Mac 4 / Backend B
:3001                      :3002
```

See [`architecture/request_flow.md`](architecture/request_flow.md) for the detailed flow.

## Repository Structure

```text
Team_1.1.1.1/
├── README.md
├── architecture/
│   ├── ip_table.md
│   ├── network_topology.md
│   ├── request_flow.md
│   └── dhcp_notes.md
├── configuration/
│   ├── dnsmasq.conf
│   ├── backend.conf
│   ├── TLS-notes.md
│   └── backend-launch-instructions.md
├── backends/
│   ├── backend-a/server.py
│   └── backend-b/server.py
├── evidence/
│   ├── 01-lan/
│   ├── 02-dns/
│   ├── 03-backends/
│   ├── 04-https-tls/
│   ├── 05-load-balancing/
│   ├── 06-http-cache/
│   ├── 07-wireshark/
│   └── 08-failure-tests/
├── captures/
│   └── mac4_capture.pcapng
└── _submission_/
    └── Backend-Source-Code.zip
```

## Running the Backends

### Backend A — Mac 3

```bash
cd backends/backend-a
python3 server.py
```

Verify:

```bash
curl -i http://127.0.0.1:3001/
curl -i http://127.0.0.1:3001/api/status
```

### Backend B — Mac 4

```bash
cd backends/backend-b
python3 server.py
```

Verify:

```bash
curl -i http://127.0.0.1:3002/
curl -i http://127.0.0.1:3002/api/status
```

## Nginx

Active Homebrew paths used on Mac 2:

```text
Main config: /opt/homebrew/etc/nginx/nginx.conf
Team 1.1.1.1 site config: /opt/homebrew/etc/nginx/servers/backend.conf
Certificate: /opt/homebrew/etc/nginx/certs/app.team1.test.crt
Private key: /opt/homebrew/etc/nginx/certs/app.team1.test.key
```

Team 1.1.1.1 site configuration: [`configuration/backend.conf`](configuration/backend.conf).

Validate and reload:

```bash
nginx -t
sudo nginx -s reload
```

## DNS

`dnsmasq` provides local A records for both Team 1.1.1.1 names and forwards normal public DNS queries upstream. Tests include Team 1.1.1.1 names and a public name (`example.com`).

See [`configuration/dnsmasq.conf`](configuration/dnsmasq.conf).

## HTTPS / TLS

TLS details:

- Subject: `C=IN, O=Team1, CN=app.team1.test`
- Issuer: `C=IN, O=Team1, CN=Team1 Local CA`
- TLS 1.3 negotiated
- Cipher observed in Wireshark: `TLS_CHACHA20_POLY1305_SHA256`
- ALPN: HTTP/1.1

The private key must **not** be committed to GitHub.

## Load Balancing

Repeated HTTPS requests produced alternating backend headers:

```text
X-Backend: B
X-Backend: A
X-Backend: B
X-Backend: A
X-Backend: B
X-Backend: A
```

The alternating responses show round-robin load balancing when both upstreams are available.

## HTTP Cache Validation

The root resource uses:

```text
Cache-Control: public, max-age=30
ETag: "team1-home-v1"
```

A request containing:

```text
If-None-Match: "team1-home-v1"
```

returns `304 Not Modified`.

The `/api/status` endpoint is sent with `Cache-Control: no-store`.

## Wireshark Findings

Packet capture summary:

| Stage | Packet | Observation |
|---|---:|---|
| DNS query | 1439 | `10.7.1.23 -> 10.7.1.82`, `A app.team1.test` |
| DNS response | 1463 | `app.team1.test -> 10.7.20.19` |
| TCP SYN | 2307 | client to `10.7.20.19:8443` |
| TCP SYN/ACK | 2321 | reverse proxy response |
| TCP ACK | 2324 | 3-way handshake complete |
| TLS Client Hello | 2327 | SNI `app.team1.test` |
| TLS Server Hello | 2330 | TLS 1.3 / CHACHA20-POLY1305-SHA256 |
| Forwarded HTTP GET | 2365 | proxy to Backend B, `X-Forwarded-Proto: https` |
| Backend response | 2368 | `HTTP/1.0 200 OK`, `X-Backend: B` |

See `evidence/07-wireshark/` and `captures/mac4_capture.pcapng`.

## Failure Tests

The following scenarios were completed:

- Wrong destination port (`8444`) -> connection refused
- One backend unavailable -> service remains available through Backend B
- Both backends unavailable -> Nginx `504 Gateway Time-out`
- Wrong DNS server -> DNS query times out
- Wrong DNS record / mapping -> client reaches the wrong host and HTTPS connection fails

See [`evidence/08-failure-tests/README.md`](evidence/08-failure-tests/README.md).

Screenshot evidence is included for all five failure scenarios.

## Phase 1 Checklist

- [x] Four-Mac LAN connectivity documented
- [x] DNS server operational
- [x] `app.team1.test` resolution verified
- [x] `api.team1.test` resolution verified
- [x] Public DNS forwarding verified
- [x] Backend A operational
- [x] Backend B operational
- [x] Nginx reverse proxy operational
- [x] Round-robin load balancing verified
- [x] HTTPS/TLS verified
- [x] Trusted local CA verified
- [x] HTTP cache validation verified
- [x] Wireshark DNS/TCP/TLS/HTTP analysis completed
- [x] Failure testing completed

## Security Note

Do not commit the TLS private key (`app.team1.test.key`) or any other private key material. The repository documents the path only.
