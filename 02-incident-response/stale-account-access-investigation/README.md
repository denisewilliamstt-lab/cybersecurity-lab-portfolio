# Unauthorized Payroll Access: Stale Contractor Account Investigation

## Executive Summary

This project analyzes an access-control incident involving a former contractor whose administrator account remained active years after the contract ended. On October 3, 2023, the account associated with Robert Taylor Jr. accessed a payroll system from IP address `152.207.255.255`, even though the contractor's engagement ended in 2019.

The central control failure was inadequate identity and access management. The organization did not revoke access when the business relationship ended, allowed a contractor to retain administrative privileges, and lacked sufficient safeguards to prevent or challenge the later login.

## Incident Facts

| Evidence Field | Observation |
|---|---|
| Event date | October 3, 2023 |
| Account holder | Robert Taylor Jr. |
| Recorded role | Legal / Administrator |
| Source IP address | `152.207.255.255` |
| Target resource | Payroll system |
| Contract end date | 2019 |
| Account status at incident | Still active with administrative access |

## Security Question

Why was an account belonging to a contractor whose engagement ended in 2019 able to authenticate to a sensitive payroll system in 2023 with administrator privileges?

## Authorization and Authentication Issues

### 1. Failed account deprovisioning

The organization did not disable or remove the contractor's account when the contract ended. This created an orphaned or stale identity capable of being used long after any legitimate business need had expired.

### 2. Excessive privileges

The account was assigned an administrator role. A contractor working with legal resources should not automatically receive unrestricted access to payroll or other unrelated sensitive systems.

### 3. Missing access expiration

No automatic expiration date appears to have been connected to the contract end date. Time-limited access would have disabled the account without depending solely on a manual offboarding step.

### 4. Weak authentication safeguards

The successful login suggests that a password alone may have been sufficient. Multi-factor authentication and risk-based login controls could have stopped or challenged the access even if the password had been retained, guessed, or compromised.

### 5. Insufficient access review

A periodic review should have detected an active contractor account with unnecessary administrator privileges during the four-year period between contract termination and the incident.

## Preliminary Risk Assessment

| Risk | Likelihood | Impact | Rationale |
|---|---|---|---|
| Unauthorized payroll-data access | High | High | A stale privileged account successfully reached a sensitive system. |
| Employee privacy exposure | High | High | Payroll systems commonly contain personal and financial information. |
| Fraudulent payroll changes | Moderate | High | Administrator privileges may allow changes as well as viewing. |
| Credential compromise | Moderate | High | The login could represent use by the former contractor or an attacker using the account. |
| Compliance and audit failure | High | High | Failure to remove terminated users violates common access-control expectations. |

## Important Investigative Limitation

The login record proves that the account was used, but it does not prove who controlled it at the time. The former contractor may have logged in, another person may have retained the credentials, or an attacker may have compromised the account. The IP address is an investigative lead, not identity proof.

## Immediate Response Actions

### Containment

1. Disable the account and revoke all active sessions, tokens, API keys, and recovery methods.
2. Remove the account from administrator and payroll-access groups.
3. Block further authentication while preserving relevant evidence.
4. Review other former employees and contractors for active accounts.

### Investigation

5. Preserve authentication, authorization, payroll, VPN, endpoint, and identity-provider logs.
6. Determine whether `152.207.255.255` is associated with an approved location, VPN, device, or previous user activity.
7. Review all actions performed by the account before and after the October 3 login.
8. Identify any payroll records viewed, exported, modified, or deleted.
9. Check for password resets, MFA changes, privilege escalation, new accounts, or persistence mechanisms.
10. Determine whether notification or escalation requirements apply.

### Recovery

11. Restore unauthorized payroll changes from verified records if necessary.
12. Rotate affected credentials and secrets.
13. Validate the access rights of every privileged payroll user.
14. Increase monitoring for suspicious identity and payroll activity.

## Corrective Action Plan

| Priority | Recommendation | Security Benefit |
|---:|---|---|
| Critical | Immediately disable accounts when employment or contracts end. | Removes access when the business need ends. |
| Critical | Integrate HR and vendor records with identity-management workflows. | Triggers consistent joiner, mover, and leaver actions. |
| Critical | Require MFA for payroll, administrative, and remote access. | Reduces misuse of stolen or retained passwords. |
| High | Assign expiration dates to contractor accounts. | Prevents indefinite access if manual offboarding fails. |
| High | Apply role-based access control and least privilege. | Limits contractors to approved systems and actions. |
| High | Use separate privileged accounts for administrative tasks. | Prevents everyday identities from retaining broad power. |
| High | Perform quarterly access certifications. | Detects stale, excessive, and inappropriate privileges. |
| Medium | Alert on dormant-account reactivation and former-user logins. | Enables rapid investigation of unusual authentication. |
| Medium | Restrict payroll access by approved device, network, or risk profile. | Adds context-aware protection around sensitive systems. |

## Recommended Account-Lifecycle Standard

### Provisioning

- Document the sponsor, role, approved resources, and business justification.
- Grant the minimum required privileges.
- Require MFA enrollment before access begins.
- Set an expiration date for every contractor identity.

### Active use

- Log authentication and privileged actions.
- Review access after role or project changes.
- Disable dormant accounts after a defined period.
- Require separate approval for payroll or administrative access.

### Offboarding

- Disable the identity at the contract end time.
- Revoke sessions, tokens, credentials, and physical access.
- Remove group memberships and application entitlements.
- Transfer owned data and resources to an authorized manager.
- Record and verify completion of every offboarding task.

## Key Takeaways

- Authentication confirms that valid credentials were presented; it does not prove that the expected person used them.
- Authorization must restrict what an authenticated identity can access.
- Contractor accounts should expire automatically and never remain active indefinitely.
- Administrative access should be exceptional, justified, monitored, and reviewed.
- Access reviews are a necessary backup when an offboarding process fails.
- IP addresses support attribution and scoping but should be evaluated alongside device, VPN, identity, and activity logs.

## Skills Demonstrated

- Access-control incident analysis
- Authentication and authorization assessment
- Identity lifecycle management
- Least-privilege analysis
- Evidence identification and preservation
- Incident containment and recovery planning
- Risk-based recommendations
- Technical reporting

## Project Note

This portfolio project is based on a fictional cybersecurity training scenario. The investigative analysis and corrective-action plan were prepared as an original professional assessment.
