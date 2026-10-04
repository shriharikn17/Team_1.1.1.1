# TLS Notes

## Active Nginx Paths on Mac 2

```text
Main Nginx config: /opt/homebrew/etc/nginx/nginx.conf
Team 1.1.1.1 site config: /opt/homebrew/etc/nginx/servers/backend.conf
Server certificate: /opt/homebrew/etc/nginx/certs/app.team1.test.crt
Server private key: /opt/homebrew/etc/nginx/certs/app.team1.test.key
```

The private key must not be committed to a public repository.

## Certificate Details

```text
Subject: C=IN; O=Team1; CN=app.team1.test
Issuer:  C=IN; O=Team1; CN=Team1 Local CA
Validity: 29 Sep 2026 to 29 Sep 2027
```

## TLS Details

Wireshark and curl show:

```text
TLS version: TLS 1.3
Cipher: TLS_CHACHA20_POLY1305_SHA256
ALPN: http/1.1
SNI: app.team1.test
```

A trusted-client test produced `SSL certificate verify ok.` after the local CA was installed/trusted.
