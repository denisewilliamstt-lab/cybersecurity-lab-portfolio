# SOC Incident Report: Suspected TCP SYN Port Scan

**Investigation date:** November 11, 2026  
**Environment:** Synthetic training PCAP  
**Classification:** Suspected reconnaissance / TCP SYN port scan  
**Provisional severity:** Low–Medium (depends on authorization, asset criticality, and surrounding telemetry)  
**Status:** Analysis complete; no confirmed compromise

## Executive summary
A Wireshark investigation of 120 simulated network packets identified a concentrated series of TCP SYN connection attempts from `198.51.100.77` toward `10.20.2.20` across different destination ports. Reset responses from the target support a TCP port-scanning interpretation. The capture does not establish unauthorized access or a completed compromise.

## Observations
| Observation | Count | Interpretation |
|---|---:|---|
| All captured packets | 120 | Entire synthetic capture |
| Initial SYN (SYN=1, ACK=0) | 51 | Connection initiation packets from all sources |
| SYN-ACK (SYN=1, ACK=1) | 23 | Willingness to establish TCP connections; not proof of completed sessions |
| RST (RST=1) | 30 | Connection resets; context needed to determine why |
| SYN involving 198.51.100.77 | 30 | Focused activity associated with suspected scanning source |

These filter counts describe overlapping or distinct TCP flag subsets as observed; they are not a complete per-session reconstruction. In particular, 23 SYN-ACK packets do not establish 23 completed connections.

## Notable addresses
- **Suspected scanner:** `198.51.100.77` (reserved documentation address; simulated)
- **Target:** `10.20.2.20` (private/internal address)
- **Additional internal traffic:** Other `10.20.1.x` sources were visible in the capture, including activity involving ports 22, 80 and 443.

## Assessment
Thirty initial SYN attempts associated with the suspected source targeted different ports on one host, with reset responses observed from the target. This pattern is consistent with TCP SYN port scanning, a reconnaissance technique used to identify reachable services. It could also represent authorized scanning. The available evidence does not confirm exploit execution, credential compromise, data access, or exfiltration.

## Recommended SOC actions
1. Confirm whether the source was an approved scanner or test.
2. Review firewall, IDS/IPS, endpoint and service logs for corresponding connections and alerts.
3. Determine whether any TCP handshakes completed, and whether suspicious follow-on activity occurred.
4. Assess the target's asset criticality and exposure; escalate according to the organization's playbook.
5. Preserve the PCAP, relevant screenshots, timestamps, and investigation notes.

## Limitations
This is a small synthetic capture. There is no independent identity, endpoint, authorization, or application telemetry. No real-world attribution is possible from reserved documentation IP space. The screenshots and original PCAP have not yet been published with this report.
