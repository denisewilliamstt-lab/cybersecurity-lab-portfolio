# Wireshark Network Intrusion Investigation — TCP Port Scan

**Type:** Simulated SOC investigation | **Tool:** Wireshark | **Status:** Analysis complete; screenshot/PCAP publication pending

## Scenario
Investigate a synthetic 120-packet network capture for suspicious TCP activity, distinguish connection attempts from completed sessions, and document defensible conclusions.

## Key findings
- 120 packets in the capture.
- Display filter for initial TCP SYN packets matched 51 packets.
- SYN-ACK filter matched 23 packets.
- TCP reset (RST) filter matched 30 packets.
- A focused filter matched 30 SYN packets involving simulated external source `198.51.100.77`, targeting internal host `10.20.2.20` across multiple destination ports.
- The target sent reset responses toward the scanning source. Multiple destination ports and reset responses support a **TCP SYN port-scanning pattern**.
- **No successful compromise is established.** Authorization status and subsequent activity are unknown.

> Note: `198.51.100.77` is in TEST-NET-2, reserved for documentation. This is simulated evidence, not a real-world attacker attribution.

## Investigation workflow
1. Open synthetic PCAP in Wireshark.
2. Filter initial SYN packets and inspect sources, destinations and ports.
3. Review TCP Conversations for source/port patterns; note that display filters can hide response packets.
4. Examine SYN-ACK and RST traffic separately.
5. Focus on the suspected scanning source and correlate the request/response pattern.
6. Assess impact and limitations; document recommendations.

## Evidence
See [incident report](./incident-report.md) and [Wireshark filters](./filters.md).

**Screenshots and original PCAP:** Not yet uploaded. Add only the synthetic PCAP and relevant screenshots after verifying they contain no personal or sensitive information.

## Skills demonstrated
TCP/IP, TCP flags, Wireshark display filters, network reconnaissance identification, evidence-based SOC reporting, and distinguishing suspicious activity from confirmed compromise.
