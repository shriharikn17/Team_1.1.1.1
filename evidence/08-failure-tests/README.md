# Failure Tests

For the failure-test run, DHCP had assigned the following addresses to the systems used for the client/proxy path:

```text
Mac 2 / Nginx:     10.7.23.20
Mac 4 / Backend B: 10.7.19.25
```

Each failure condition was isolated so the expected behavior could be observed without changing the documented production topology. DNS-related tests used `dig` or `curl --resolve` to control name resolution during the test.

## 1. Wrong destination port

The correct HTTPS service port is `8443`. The client deliberately attempted `8444`:

```bash
curl -vk \
  --resolve app.team1.test:8444:10.7.23.20 \
  --connect-timeout 5 \
  https://app.team1.test:8444/
```

Observed result: connection refused.

Evidence: `01_wrong_destination_port.png`

## 2. One backend unavailable

Backend A was intentionally unavailable while Backend B remained healthy. Six HTTPS requests all returned:

```text
HTTP/1.1 200 OK
X-Backend: B
```

This shows that Nginx continued serving traffic through the remaining healthy backend.

Evidence: `02_one_backend_down.png`

## 3. Both backends unavailable

Both upstream backends were made unavailable for this test.

Observed result:

```text
HTTP/1.1 504 Gateway Time-out
Server: nginx/1.31.6
```

This shows that the reverse proxy remained reachable but had no usable upstream server.

Evidence: `03_both_backends_down.png`

## 4. Wrong DNS server

A DNS query was deliberately sent to Mac 2 / Nginx, which is not the DNS server:

```bash
dig @10.7.23.20 app.team1.test +time=2 +tries=1
```

Observed result:

```text
connection timed out; no servers could be reached
```

Evidence: `04_wrong_dns_server.png`

## 5. Wrong DNS record / host mapping

The application hostname was deliberately mapped to Backend B's host IP instead of the Nginx reverse proxy:

```bash
curl -vk \
  --resolve app.team1.test:8443:10.7.19.25 \
  --connect-timeout 5 \
  https://app.team1.test:8443/
```

The request timed out because `10.7.19.25` does not provide the HTTPS service on port `8443`.

Evidence: `05_wrong_dns_record.png`
