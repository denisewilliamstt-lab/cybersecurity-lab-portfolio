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

## Analyst walkthrough — screenshot-by-screenshot

These screenshots document **Splunk setup and log ingestion**. They do not show the searches that produced the incident findings. The SPL queries and conclusions are documented above, but search-results screenshots would strengthen the evidence. This is a synthetic training investigation, not a confirmed real-world compromise.

### 1. Splunk workspace opened

The Splunk Enterprise home screen establishes the tool used for the lab. This is preparation, not a security detection result.

### 2. Authentication CSV selected

The Add Data workflow shows the synthetic bank authentication CSV selected for upload. This is the first ingestion step.

### 3. CSV rows previewed

The Set Source Type screen shows the CSV data in rows and columns. Previewing the records helps check that Splunk can read the dataset before indexing.

### 4. Input settings reviewed — close-up

This close-up shows the host and index configuration controls. It documents the configuration stage, not an executed search.

### 5. Input settings reviewed — full view

This wider view shows the Input Settings page with the bank_security index selected, indicating the destination for the simulated authentication events.

**How the investigation connects:** After ingestion, the analyst can search `index=bank_security` to summarize login results, investigate failures for `j.smith`, and review the sequence of failed VPN logins, subsequent success, and MFA change. The report records those queries and findings; the screenshots here demonstrate only the preceding setup stages.

## Portfolio notes
This is a fictional training case, not a production incident. Five Splunk setup screenshots are included below and stored alongside this report. The report separates observed events from hypotheses and recommendations.


## Screenshot evidence

### 1. Splunk workspace opened

The Splunk Enterprise home screen establishes the tool used for the lab. This is preparation, not a security detection result.

![Splunk workspace opened](<Screenshot%202026-11-10%20065814.png>)

### 2. Authentication CSV selected

The Add Data workflow shows the synthetic bank authentication CSV selected for upload. This is the first ingestion step.

![Authentication CSV selected](<Screenshot%202026-11-10%20070318.png>)

### 3. CSV rows previewed

The Set Source Type screen shows the CSV data in rows and columns. Previewing the records helps check that Splunk can read the dataset before indexing.

![CSV rows previewed](<Screenshot%202026-11-10%20070520.png>)

### 4. Input settings reviewed — close-up

This close-up shows the host and index configuration controls. It documents the configuration stage, not an executed search.

![Input settings reviewed — close-up](<Screenshot%202026-11-10%20at%2007-07-37%20Add%20Data%20-%20Input%20Settings%20Splunk%2010.6.1.1(1).png>)

### 5. Input settings reviewed — full view

This wider view shows the Input Settings page with the bank_security index selected, indicating the destination for the simulated authentication events.

![Input settings reviewed — full view](<Screenshot%202026-11-10%20070952.png>)

## Reproducibility and evidence guide

**Step-by-step method:** Document the GUI upload and CSV preview, then map each recorded SPL query to its investigation purpose: count failures, isolate j.smith, and reconstruct the VPN/MFA sequence.

**Commands or filters:** Use the exact commands, SQL, filters, or methodology already documented in this project. GUI actions should be described as clicks/settings, not invented code. Any new command must be identified as a suggested follow-up until actually executed.

**Screenshot checkpoint:** Capture actual Splunk search bar and results for failed-login counts, j.smith timeline, and suspicious-IP correlation. The five existing images show ingestion, not search output.

**Analyst explanation:** For each real result, explain what it demonstrates, why it matters to security, and what cannot be concluded. Missing screenshots remain an evidence gap; do not fabricate them.
