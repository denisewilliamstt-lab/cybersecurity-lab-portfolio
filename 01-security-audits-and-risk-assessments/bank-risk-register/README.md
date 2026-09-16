# Bank Cybersecurity Risk Register

## Project Overview

This project evaluates operational, cybersecurity, physical, and third-party risks affecting a fictional community bank. A qualitative risk register was used to rank each risk according to its likelihood and potential business impact.

The purpose of the assessment was to help decision-makers focus limited security resources on the risks that could cause the greatest harm to customer data, financial records, funds, regulatory compliance, and daily operations.

## Operational Environment

The bank operates in a coastal area with a relatively low crime rate. Its environment includes:

- 100 employees working on-site
- 20 remote employees
- 2,000 individual customer accounts
- 200 commercial customer accounts
- Marketing relationships with a professional sports team and ten local businesses
- Strict financial regulations governing the protection and availability of data and funds
- Daily cash-availability obligations connected to Federal Reserve requirements

The bank's combination of employees, customers, systems, business partners, and regulatory duties creates a broad risk surface. Its coastal location also makes business continuity and third-party delivery dependencies important considerations.

## Risk-Scoring Method

Each risk was scored using two factors:

- **Likelihood:** The probability that the weakness will be exploited or the event will occur.
- **Severity:** The potential damage to the bank if the event occurs.

Both factors use a scale from 1 to 3:

| Score | Likelihood | Severity |
|---|---|---|
| 1 | Rare | Low |
| 2 | Likely | Moderate |
| 3 | Certain or highly likely | Catastrophic |

The priority score was calculated as:

```text
Risk Priority = Likelihood × Severity
```

| Priority Score | Suggested Response Level |
|---|---|
| 1–2 | Low: monitor or accept with documented justification |
| 3–4 | Moderate: plan and implement reasonable controls |
| 6 | High: address promptly and track remediation |
| 9 | Critical: begin immediate corrective action |

## Risk Register

| Rank | Asset | Risk | Vulnerability or Scenario | Likelihood | Severity | Priority |
|---:|---|---|---|---:|---:|---:|
| 1 | Financial records | Data leak | A backup database server is publicly accessible. | 3 | 3 | **9 – Critical** |
| 2 | User database | Data compromise | Customer information is protected with inadequate encryption. | 2 | 3 | **6 – High** |
| 3 | Funds | Business email compromise | An employee is manipulated into disclosing confidential information or authorizing fraudulent activity. | 2 | 2 | **4 – Moderate** |
| 4 | Physical funds | Theft | The bank's safe is left unlocked. | 1 | 3 | **3 – Moderate** |
| 5 | Operations and cash availability | Supply-chain disruption | A natural disaster delays deliveries and interrupts required services. | 1 | 2 | **2 – Low** |

## Risk Analysis and Treatment Recommendations

### 1. Publicly accessible backup database — Critical

The financial-records exposure received the maximum score because the database is already publicly accessible and could contain sensitive or regulated information. A breach could cause financial losses, regulatory penalties, customer harm, and reputational damage.

**Recommended treatment:** Mitigate immediately.

- Remove public access and restrict the server to approved networks and identities.
- Apply least privilege and role-based access controls.
- Encrypt backup data at rest and in transit.
- Review access logs for evidence of prior unauthorized activity.
- Scan cloud and on-premises configurations for similar exposures.
- Establish recurring backup-security and restoration tests.

### 2. Poorly encrypted customer database — High

Weak encryption threatens the confidentiality of information belonging to 2,200 individual and commercial customers. The high severity reflects the financial, legal, and trust consequences of exposing regulated customer data.

**Recommended treatment:** Mitigate promptly.

- Replace outdated or weak encryption with current approved standards.
- Protect encryption keys separately and rotate them on a defined schedule.
- Encrypt data both at rest and during transmission.
- Restrict database access according to job responsibility.
- Conduct periodic vulnerability assessments and access reviews.

### 3. Business email compromise — Moderate

The bank has 120 employees operating in on-site and remote environments. Attackers could impersonate executives, vendors, or business partners to steal information or redirect funds. External marketing partnerships create additional trusted relationships that could be abused through social engineering.

**Recommended treatment:** Mitigate.

- Require multi-factor authentication for email and financial systems.
- Provide phishing and social-engineering awareness training.
- Require secondary verification for unusual payment or data requests.
- Implement email filtering and domain-protection controls such as SPF, DKIM, and DMARC.
- Create a clear process for reporting suspicious messages.

### 4. Unlocked bank safe — Moderate

Although the surrounding area has low crime rates, leaving a safe unlocked creates an unnecessary physical-security weakness. The likelihood is low, but the potential loss of funds makes the impact severe.

**Recommended treatment:** Mitigate with straightforward physical controls.

- Keep the safe locked whenever authorized personnel are not actively accessing it.
- Limit access to designated employees.
- Maintain access records and dual-control procedures.
- Use CCTV coverage and alarms around restricted areas.
- Perform opening and closing security checks.

### 5. Natural-disaster supply-chain disruption — Low

The coastal location introduces exposure to storms and other natural hazards. Although the assessed likelihood and severity are lower, delivery delays could affect cash availability and the bank's ability to meet operational or regulatory obligations.

**Recommended treatment:** Monitor and reduce dependency.

- Maintain alternative suppliers and delivery arrangements.
- Establish business-continuity and disaster-recovery procedures.
- Define minimum cash and critical-supply thresholds.
- Test communication procedures with vendors and regulators.
- Review coastal hazard exposure periodically.

## Third-Party Risk Considerations

Relationships with a professional sports team and ten local businesses expand the number of potential routes through which data or trusted communications might be compromised. Before granting a partner access to information or systems, the bank should:

- Perform security due diligence.
- Define data-handling and incident-notification requirements in contracts.
- Grant only the minimum access needed.
- Review partner access regularly.
- Revoke access immediately when the relationship ends or requirements change.

## Priority Action Plan

| Time Frame | Action |
|---|---|
| Immediate | Isolate the exposed backup database, investigate prior access, and secure the data. |
| Immediate | Strengthen customer-database encryption and restrict access. |
| 30 days | Implement or confirm MFA, payment verification, and phishing-reporting controls. |
| 30 days | Enforce safe-access procedures and dual control. |
| 60–90 days | Review third-party access and contractual security requirements. |
| 60–90 days | Test disaster-recovery and alternate-supplier procedures. |
| Ongoing | Reassess risks after control changes, incidents, or significant business changes. |

## Conclusion

The risk register shows that the bank should first address the exposed backup server and inadequate customer-data encryption. These risks combine high likelihood with catastrophic potential impact. Business email compromise and physical security require additional controls, while supply-chain disruption should remain part of the bank's continuity planning because of its coastal location and regulatory cash-availability obligations.

Risk scores support prioritization, but they should not be treated as permanent. The bank should review the register regularly and calculate residual risk after safeguards are implemented.

## Skills Demonstrated

- Cybersecurity risk identification
- Qualitative likelihood and impact scoring
- Risk prioritization
- Risk treatment recommendations
- Data-protection analysis
- Third-party risk assessment
- Business-continuity planning
- Technical and executive documentation

## Project Note

This portfolio project is based on a fictional financial-services scenario completed during cybersecurity training. The analysis, prioritization, and recommendations were prepared as an original professional assessment.
