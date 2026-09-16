# Botium Toys: Security Audit and Compliance Assessment

## Project Overview

This project documents an internal security audit for Botium Toys, a fictional U.S. toy retailer with a physical office, storefront, warehouse, and growing international e-commerce operation. The assessment reviews the organization's security controls and its alignment with PCI DSS, GDPR, and SOC expectations.

The audit was performed using the National Institute of Standards and Technology Cybersecurity Framework (NIST CSF) as an organizing framework. Its purpose was to identify control gaps, evaluate compliance exposure, and recommend actions that would reduce risk to customer information, business systems, and operations.

## Audit Scope

The review covered assets and processes managed by the IT department, including:

- On-premises equipment and physical facilities
- Employee workstations and company systems
- Network infrastructure and internet-facing services
- Customer and employee data
- Payment-card information and online transaction processes
- Policies, procedures, and business-continuity practices
- Legacy systems and their maintenance

## Audit Objectives

- Evaluate existing administrative, technical, and physical controls.
- Identify risks affecting confidentiality, integrity, and availability.
- Review alignment with PCI DSS, GDPR, and SOC best practices.
- Recommend prioritized improvements to the company's security posture.

## Risk Summary

Botium Toys has several useful physical and technical safeguards, including a firewall, antivirus software, locks, CCTV, and fire-detection systems. However, its overall risk exposure remains high because sensitive data is broadly accessible, encryption is absent, password requirements are weak, and formal recovery controls have not been established.

The most significant risks are unauthorized access to customer and payment data, operational disruption after an incident, regulatory penalties, and fraud caused by insufficient separation of duties.

## Controls Assessment

| Control | Status | Assessment |
|---|---|---|
| Least privilege | Not implemented | Employees have broader access to customer data than their job duties require. Role-based access should restrict sensitive information. |
| Disaster recovery plan | Not implemented | No formal recovery plan exists, creating a serious business-continuity risk after an outage or cyber incident. |
| Password policy | Inadequate | Minimum password requirements are weak and increase the likelihood of account compromise. |
| Separation of duties | Not implemented | Concentrating operational and payroll responsibilities with one executive increases the risk of error and fraud. |
| Firewall | Implemented | Network traffic is filtered using established security rules. |
| Intrusion detection system | Not implemented | The organization lacks automated detection of suspicious network activity and potential intrusions. |
| Backups | Not implemented | Critical information is not adequately protected by a defined backup and restoration process. |
| Antivirus software | Implemented | Antivirus software is installed and monitored by the IT department. |
| Legacy-system maintenance | Partially implemented | Legacy systems are monitored, but maintenance schedules and intervention procedures are not formally documented. |
| Encryption | Not implemented | Sensitive information is not encrypted, increasing confidentiality and breach risk. |
| Password manager | Not implemented | A centralized password-management solution is unavailable. |
| Physical locks | Implemented | The office, storefront, and warehouse have appropriate physical locks. |
| CCTV surveillance | Implemented | Video surveillance is installed and operational at the physical location. |
| Fire detection and prevention | Implemented | Fire alarms and prevention systems are present and functional. |

## Compliance Assessment

### Payment Card Industry Data Security Standard (PCI DSS)

| Best Practice | Status | Finding |
|---|---|---|
| Restrict cardholder data to authorized users | Not met | Internal access is not limited according to job responsibility. |
| Securely process, transmit, and store card data | Not met | Broad employee access and the absence of encryption expose payment information. |
| Encrypt payment data and transaction touchpoints | Not met | Encryption controls have not been implemented. |
| Maintain secure password-management practices | Not met | Password policies are weak, and no password manager is in place. |

### General Data Protection Regulation (GDPR)

| Best Practice | Status | Finding |
|---|---|---|
| Protect and secure E.U. customer data | Not met | Sensitive customer information is not encrypted. |
| Notify affected E.U. customers within 72 hours | Met | A breach-notification plan is in place. |
| Classify and inventory data | Partially met | Assets are inventoried but have not been classified by sensitivity or criticality. |
| Maintain privacy policies and procedures | Met | Privacy processes have been developed and communicated to relevant employees. |

### System and Organization Controls (SOC)

| Best Practice | Status | Finding |
|---|---|---|
| Establish user-access policies | Not met | Least privilege and separation of duties are not enforced. |
| Keep PII and sensitive PII confidential | Not met | Sensitive data lacks encryption and adequate access restrictions. |
| Maintain data integrity | Met | Controls support the consistency, completeness, accuracy, and validation of data. |
| Limit data availability to authorized personnel | Not met | Data is available beyond the employees who require it for their roles. |

## Prioritized Recommendations

### Immediate Priority

1. Enforce least privilege through role-based access control and periodic access reviews.
2. Encrypt sensitive customer, employee, and payment data both at rest and in transit.
3. Establish a disaster recovery plan and tested backup-and-restoration procedures.
4. Strengthen password requirements and deploy a password manager with multi-factor authentication where possible.

### Near-Term Priority

5. Separate payroll, operational, and approval responsibilities to reduce fraud risk.
6. Deploy an intrusion detection or prevention capability and define an alert-review process.
7. Classify data according to sensitivity, regulatory requirements, and business criticality.
8. Document a recurring maintenance and intervention schedule for legacy systems.

### Ongoing Governance

9. Perform periodic access, control, and compliance reviews.
10. Test recovery procedures and breach-notification processes through tabletop exercises.
11. Provide recurring security-awareness training and document employee acknowledgment of policies.

## Conclusion

Botium Toys has foundational safeguards, particularly for physical security and basic endpoint and network protection. Its largest weaknesses involve identity and access management, data protection, monitoring, and resilience. Addressing the immediate priorities would substantially reduce the likelihood and impact of unauthorized access, data exposure, operational interruption, and compliance penalties.

## Skills Demonstrated

- Security auditing
- Risk identification and prioritization
- NIST CSF application
- Controls assessment
- PCI DSS, GDPR, and SOC compliance analysis
- Security recommendations and technical documentation

## Project Note

This portfolio project is based on a fictional case study completed during cybersecurity training. The analysis and wording in this report were prepared as an original professional summary of the assessment.
