# End-to-End Request Flow

1. The client asks the configured Team 1.1.1.1 DNS server for `app.team1.test`.
2. `dnsmasq` returns the IP of Mac 2, the Nginx reverse proxy.
3. The client establishes a TCP connection to Nginx HTTPS port `8443`.
4. TLS negotiation occurs; Wireshark shows SNI `app.team1.test` and TLS 1.3.
5. Nginx terminates TLS and selects an upstream using its `backend_servers` group.
6. Nginx forwards the request over HTTP to Backend A (`:3001`) or Backend B (`:3002`).
7. Forwarding headers preserve request metadata:

```text
Host: app.team1.test
X-Real-IP: <client IP>
X-Forwarded-For: <client IP>
X-Forwarded-Proto: https
```

8. The selected backend returns HTML or JSON and an `X-Backend` header.
9. Nginx relays the response to the HTTPS client.

## Packet-Capture Example

```text
10.7.1.23 -> 10.7.1.82       DNS A? app.team1.test
10.7.1.82 -> 10.7.1.23       DNS A 10.7.20.19
10.7.1.23 -> 10.7.20.19:8443 TCP SYN
10.7.20.19 -> 10.7.1.23      TCP SYN, ACK
10.7.1.23 -> 10.7.20.19      TCP ACK
10.7.1.23 -> 10.7.20.19      TLS Client Hello, SNI=app.team1.test
10.7.20.19 -> 10.7.1.23      TLS Server Hello, TLS 1.3
10.7.20.19 -> 10.7.1.23:3002 HTTP GET / (forwarded request)
10.7.1.23:3002 -> 10.7.20.19 HTTP/1.0 200 OK, X-Backend: B
```
