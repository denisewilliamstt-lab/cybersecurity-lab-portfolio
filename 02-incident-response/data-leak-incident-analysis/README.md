# Data Leak Incident Analysis: Least-Privilege Failure

## Executive Summary

This project analyzes a data leak caused by excessive folder permissions, failure to revoke temporary access, and accidental sharing with an external business partner. The exposed folder contained internal information about an unannounced product, customer analytics, and promotional materials.

The primary control failure was a violation of the principle of least privilege. The incident maps to the NIST Cybersecurity Framework data-security outcome `PR.DS-5` and the least-privilege control in NIST SP 800-53 `AC-6`.

## Incident Scenario

A sales manager gave the sales team access to a folder of internal-only documents during a meeting. The folder contained:

- Information about a product that had not been publicly announced
- Customer analytics
- Promotional materials

After the meeting, the manager left the team's access in place and instructed employees not to distribute the promotional content until approval was granted.

Later, a sales representative intended to give a business partner a link to the approved promotional materials. The representative accidentally shared the link to the entire internal folder. The partner believed the link contained authorized promotional content and posted it on the company's social-media page, exposing the internal documents publicly.

## Incident Timeline

| Stage | Event |
|---:|---|
| 1 | A manager grants the sales team access to an internal folder. |
| 2 | The manager does not revoke or time-limit access after the meeting. |
| 3 | Employees are warned verbally not to share promotional materials without approval. |
| 4 | A sales representative mistakenly sends the internal-folder link to a business partner. |
| 5 | The partner assumes the content is approved and publishes the link on social media. |
| 6 | Unannounced product information and customer analytics become publicly accessible. |

## Affected Information

| Information | Classification | Potential Impact |
|---|---|---|
| Unannounced product information | Internal or confidential | Loss of competitive advantage, premature disclosure, and reputational harm |
| Customer analytics | Confidential or restricted | Customer privacy exposure and possible regulatory or contractual consequences |
| Promotional materials | Internal until approved | Loss of messaging control and unauthorized publication |

## Root-Cause Analysis

### Primary cause: Excessive access

Access was granted to a shared folder containing more information than the team needed. The folder structure did not separate promotional materials from customer analytics and confidential product information.

### Contributing factors

- Temporary access was not revoked after its business purpose ended.
- The shared link allowed access outside the intended internal audience.
- No expiration date or automatic revocation was applied.
- The business partner was able to redistribute the link publicly.
- Verbal instructions were used in place of technical enforcement.
- The representative did not verify the link's destination or permissions before sending it.
- Sensitive information with different purposes and classifications was stored together.

## Control Mapping

| Framework Element | Mapping |
|---|---|
| NIST CSF Function | **Protect** |
| NIST CSF Category | **PR.DS: Data Security** |
| NIST CSF Subcategory | **PR.DS-5: Protections against data leaks** |
| Control Reference | **NIST SP 800-53 AC-6: Least Privilege** |

### AC-6 security principle

Users, processes, and roles should receive only the access and authorization required to complete an approved task. Access should not remain active or permit broader actions after the business need ends.

Relevant enhancements for this incident include:

- Restrict sensitive resources according to user role.
- Automatically revoke or expire access after a defined period.
- Maintain activity logs for accounts and shared resources.
- Review user privileges regularly.

## Immediate Incident-Response Actions

### Containment

1. Disable the exposed link and revoke external access immediately.
2. Ask the business partner to remove the social-media post and any copied content.
3. Restrict the folder to approved internal users.
4. Preserve sharing, access, download, and social-media evidence for investigation.

### Investigation

5. Determine how long the link was publicly available.
6. Review logs to identify viewers, downloads, forwarding, and permission changes.
7. Confirm exactly which documents and customer information were exposed.
8. Assess whether breach-notification, privacy, contractual, or legal obligations apply.

### Recovery

9. Move sensitive information into appropriately classified and permissioned locations.
10. Generate new approved links for promotional materials only.
11. Notify internal stakeholders and affected parties according to the incident-response plan.
12. Monitor for reposting, misuse of customer information, or premature product disclosures.

## Corrective Action Plan

| Priority | Corrective Action | Expected Outcome |
|---:|---|---|
| Critical | Configure shared folders as internal-only by default. | Prevents public access through copied links. |
| Critical | Separate promotional files from customer analytics and product-development information. | Limits the amount of information exposed by one mistake. |
| High | Apply role-based access control and least privilege. | Users receive only the data needed for their responsibilities. |
| High | Use expiring links and automatic access revocation. | Temporary permissions do not remain active indefinitely. |
| High | Block link resharing and downloads when the business purpose does not require them. | Reduces uncontrolled distribution. |
| Medium | Require approval before externally sharing sensitive or pre-release content. | Adds verification before disclosure. |
| Medium | Audit permissions and shared links on a recurring schedule. | Detects excessive, outdated, or public access. |
| Medium | Train employees to verify link targets, recipients, classifications, and permissions. | Reduces human error during collaboration. |

## Recommended Sharing Procedure

Before sending information outside the organization, an employee should verify:

1. **Recipient:** Is this person authorized to receive the information?
2. **Content:** Does the location contain only the intended files?
3. **Classification:** Is external distribution allowed?
4. **Permission:** Is the link view-only, restricted, and non-reshareable where possible?
5. **Expiration:** Will access end when the business need ends?
6. **Approval:** Has the appropriate manager or data owner authorized release?

## Lessons Learned

- Policy reminders alone cannot replace enforced technical controls.
- Shared folders should not combine data with different sensitivity levels and business purposes.
- Temporary permissions require expiration or a documented revocation step.
- External sharing should be denied by default and enabled only for approved content.
- Activity logs are essential for determining the scope of a disclosure.
- Business partners should receive clear handling and redistribution requirements.

## Skills Demonstrated

- Data-leak incident analysis
- Root-cause and contributing-factor identification
- Incident containment and recovery planning
- Least-privilege assessment
- NIST CSF control mapping
- NIST SP 800-53 AC-6 application
- Corrective-action planning
- Security documentation

## Project Note

This portfolio project is based on a fictional cybersecurity training scenario. The incident analysis, response actions, and corrective recommendations were prepared as an original professional assessment.
