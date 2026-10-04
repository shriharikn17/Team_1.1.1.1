# Backend Launch Instructions

## Backend A — Mac 3

```bash
cd backends/backend-a
python3 server.py
```

Service port: `3001`

Verification:

```bash
curl -i http://127.0.0.1:3001/
curl -i http://127.0.0.1:3001/api/status
```

## Backend B — Mac 4

```bash
cd backends/backend-b
python3 server.py
```

Service port: `3002`

Verification:

```bash
curl -i http://127.0.0.1:3002/
curl -i http://127.0.0.1:3002/api/status
```

## Remote Verification

Using the main lab addresses:

```bash
curl -i http://10.7.13.26:3001/
curl -i http://10.7.1.23:3002/
```
