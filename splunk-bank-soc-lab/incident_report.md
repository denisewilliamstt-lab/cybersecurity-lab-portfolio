# SOC Incident Report — Suspected Account Takeover

**Case:** BANK-SOC-001  
**Status:** Investigation complete for available simulated evidence; compromise unconfirmed  
**Severity:** High (provisional; pending account-owner verification and additional telemetry)  
**Analyst lab:** Splunk Enterprise / `bank_security`  
**Data source:** Synthetic `bank_authentication_logs.csv` (136 events)

## Executive summary
A suspicious authentication sequence targeted account `j.smith`. From a single simulated source IP (`198.51.100.24`), 24 VPN authentication failures occurred at nine-second intervals, followed by one successful VPN login. Three minutes later, a successful MFA-method change was recorded from the same IP. The account had subsequent successful web-portal authentications from internal IP addresses. This pattern warrants prompt escalation as a suspected account takeover; the dataset alone cannot establish who authenticated or what resources were accessed.

## Evidence and timeline (UTC, 2026-11-08)
| Time | Evidence |
|---|---|
| 01:15–01:51 | Initial web-portal activity for `j.smith`: 3 successes, 1 failure, from internal IPs. |
| 02:10:00–02:13:27 | 24 failed VPN logins from `198.51.100.24`, spaced nine seconds apart. |
| 02:14:00 | Successful VPN login for `j.smith` from `198.51.100.24`. |
| 02:17:00 | Successful `mfa_change` event on `identity-portal` from `198.51.100.24`. |
| 02:33 onward | Additional successful web-portal logins from `10.10.2.14`, `10.10.2.19`, and `10.10.3.21`; not proven to be the same device or actor. |

## Additional findings
- Dataset totals: 136 events, 100 successes and 36 failures.
- `j.smith` accounts for 27 of 36 failures (75%).
- The suspicious source IP targeted only `j.smith` in the available dataset.
- `198.51.100.24` is a TEST-NET documentation IP used for this simulation, not a real-world address to geolocate.

## Assessment
**Suspected automated password guessing with possible account takeover and MFA persistence.** Repeated, regularly spaced failures followed by a success and a successful MFA change are concerning. However, no account-owner confirmation, MFA challenge details, device identification, VPN session activity, endpoint logs, or file-access records are included. Do not report confirmed compromise, lateral movement, or exfiltration without evidence.

## Recommended response
1. Escalate promptly to the incident response team under the organization's playbook.
2. Confirm the login and MFA change with the account owner through a trusted channel; inspect identity-provider audit details, MFA enrollment, and device identity.
3. Preserve relevant authentication evidence and correlate VPN sessions, endpoint, network, and application logs.
4. If warranted and authorized, revoke sessions, reset credentials, and resecure MFA methods; monitor for additional suspicious access.
5. Update the incident record with ownership, response actions, outcomes, and closure criteria.

## SPL used
```spl
index=bank_security
| stats count by result
```
```spl
index=bank_security result="FAILURE"
| stats count by user
| sort - count
```
```spl
index=bank_security user="j.smith" system="vpn-gateway"
| stats count by src_ip result
```
```spl
index=bank_security user="j.smith"
| table _time src_ip result action system
| sort _time
```
```spl
index=bank_security src_ip="198.51.100.24"
| stats count by user result
| sort user
```

## Portfolio notes
This is a fictional training case, not a production incident. Screenshots may be added from Splunk for the GitHub portfolio. The report separates observed events from hypotheses and recommendations.
