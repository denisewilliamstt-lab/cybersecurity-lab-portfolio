# Splunk SIEM Lab — Suspected Account Takeover

**Portfolio project:** BANK-SOC-001 | **Tool:** Splunk Enterprise | **Dataset:** 136 synthetic authentication events

## Objective
Investigate repeated VPN authentication failures, correlate activity across systems, and assess a possible account takeover without overstating what the evidence proves.

## Key findings
- 24 failed VPN logins against `j.smith` from `198.51.100.24` at nine-second intervals
- One successful VPN login afterward
- A successful MFA-method change three minutes later from the same source IP
- Subsequent successful web-portal authentications, not attributable to the same actor from these logs alone
- **Assessment:** Suspected account takeover; **provisional high severity**; compromise **not confirmed**

## Investigation workflow
1. Identify alert and scope the authentication dataset
2. Analyze failed logins by user and source IP
3. Reconstruct the authentication timeline
4. Correlate the VPN success with the identity-portal MFA change
5. Assess impact, limitations, escalation, and authorized containment
6. Document evidence and recommendations

## Files
- [Incident report](incident_report.md) — findings, UTC timeline, SPL queries, limitations, and response recommendations
- Five setup/ingestion screenshots are embedded in the incident report.
- A November 11 evidence audit in the incident report records the actual baseline counts, failed-login concentration, and source-IP correlation, and distinguishes screenshots already in GitHub from those available only in the conversation or saved locally.
- Search-result images still need to be uploaded and linked; a screenshot of the detailed MFA-change timeline has not been verified.

## Reproduce in Splunk
Upload the synthetic CSV with the fields `timestamp,user,src_ip,result,action,system` to the `bank_security` index. Set the search time range to **All time**.

```spl
index=bank_security user="j.smith"
| table _time src_ip result action system
| sort _time
```

## Ethics and limitations
All accounts and events are fictional. `198.51.100.24` is a reserved documentation IP, not a live attacker address. Authentication logs alone do not prove unauthorized access, lateral movement, file access, or exfiltration.
