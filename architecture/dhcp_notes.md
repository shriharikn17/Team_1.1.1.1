# DHCP / Address-Change Notes

The project was tested over a WLAN that assigned addresses dynamically, so screenshots from different sessions contain different IPs for the same physical Mac.

## Addresses seen in evidence

- Mac 1 / DNS: `10.7.19.174` in the earlier setup; `10.7.1.82` in the final Wireshark capture.
- Mac 2 / Nginx: `10.7.20.19` in the baseline implementation; `10.7.23.20` during the failure-test run.
- Mac 3 / Backend A: `10.7.13.26` in the baseline setup.
- Mac 4 / Backend B: `10.7.1.23` in the baseline setup; `10.7.19.25` during the failure-test run.

When an address changed, the relevant runtime configuration was updated for that session. The logical roles, ports and request path did not change.
