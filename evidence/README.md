# Evidence Index

## 01 — LAN
Machine network details and connectivity/ping tests.

## 02 — DNS
Local `dnsmasq`, app/API private-name resolution and public DNS forwarding.

## 03 — Backends
Direct Backend A / Backend B reachability and responses.

## 04 — HTTPS / TLS
Trusted HTTPS and curl TLS details.

## 05 — Load Balancing
Repeated requests demonstrating alternating `X-Backend: A/B` responses.

## 06 — HTTP Cache
ETag validation and `304 Not Modified` behavior.

## 07 — Wireshark
DNS, TCP handshake, TLS SNI/Server Hello, forwarded HTTP request/response, TCP stream and protocol statistics.

## 08 — Failure Tests
Wrong port, one backend down, both backends down, wrong DNS server and wrong DNS mapping.
