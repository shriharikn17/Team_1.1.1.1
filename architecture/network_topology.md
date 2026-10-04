# Network Topology

```mermaid
flowchart LR
    C[Client / Mac 4 test client] -->|DNS query| D[Mac 1\ndnsmasq\n:53]
    D -->|A record: app.team1.test| C
    C -->|HTTPS :8443| N[Mac 2\nNginx Reverse Proxy\nTLS Termination]
    N -->|HTTP :3001| A[Mac 3\nBackend A]
    N -->|HTTP :3002| B[Mac 4\nBackend B]
```

## Responsibilities

- **Mac 1**: local DNS and upstream DNS forwarding.
- **Mac 2**: HTTP/HTTPS entry point, TLS termination, reverse proxying and load balancing.
- **Mac 3**: Backend A application server.
- **Mac 4**: Backend B application server and client for several validation tests.
