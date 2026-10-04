# Team 1.1.1.1 Machine Roles and IP / Service Table

## Network Setup

| Machine | Member | Role | IP Address | Port | Service |
|---|---|---|---|---:|---|
| Mac 1 | Saksham Narotra | DNS | `10.7.1.82` | 53 | `dnsmasq` |
| Mac 2 | Shrihari K.N | Edge / reverse proxy / load balancer | `10.7.20.19` | 8081 / 8443 | Nginx HTTP / HTTPS |
| Mac 3 | Rachit Singh | Backend A | `10.7.13.26` | 3001 | Python HTTP backend |
| Mac 4 | Amogha Raj Sandur | Backend B / test client | `10.7.1.23` | 3002 | Python HTTP backend |

## Domain Mapping

```text
app.team1.test -> 10.7.20.19
api.team1.test -> 10.7.20.19
```

## DHCP Note

The lab WLAN assigned addresses dynamically. Earlier evidence records Mac 1 at `10.7.19.174`. During the failure-test run, Mac 2 used `10.7.23.20` and Mac 4 used `10.7.19.25`. These DHCP changes do not alter the logical architecture.
