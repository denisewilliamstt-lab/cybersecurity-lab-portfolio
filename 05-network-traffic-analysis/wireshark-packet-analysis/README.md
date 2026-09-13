# Wireshark Packet Analysis

## Project Overview

In this project, I used Wireshark to examine a packet capture file from a simulated web-browsing session. I filtered the network traffic to identify communicating systems, examine common network protocols, and locate relevant DNS and HTTP activity.

## Scenario

As a security analyst, I was asked to investigate network traffic involving a user connecting to a website. My goal was to identify the systems involved, determine which protocols were used, and examine the information transmitted between them.

This project was completed in a controlled lab environment using fictional data.

## Objectives

* Identify source and destination IP addresses
* Examine Ethernet, IPv4, TCP, UDP, DNS, HTTP, and ICMP traffic
* Filter packets by IP address, MAC address, port, and packet contents
* Inspect TCP ports and flags
* Identify DNS queries and responses
* Document relevant findings clearly

## Tools Used

* Wireshark
* Sample PCAP file
* Windows virtual machine

## Skills Demonstrated

* Packet-capture analysis
* Wireshark display filters
* Network protocol identification
* Source and destination analysis
* DNS traffic analysis
* TCP and UDP analysis
* Technical documentation

## Investigation Process

### 1. Initial Traffic Review

I opened the packet capture in Wireshark and reviewed the packet list, including the packet number, timestamp, source, destination, protocol, length, and information fields.

**Observation:**
[Describe the types of traffic you noticed before applying filters.]

### 2. IP Address Analysis

I used the following filters to examine traffic associated with a specific IP address:

```text
ip.addr == 142.250.1.139
ip.src == 142.250.1.139
ip.dst == 142.250.1.139
```

These filters allowed me to separate all traffic involving the address from packets specifically originating from or being sent to the address.

**Finding:**
[Record what you observed about the source and destination traffic.]

### 3. MAC Address and IPv4 Analysis

I filtered traffic involving a specific MAC address:

```text
eth.addr == 42:01:ac:15:e0:02
```

I then inspected the Ethernet II and IPv4 information contained inside the packet.

**Finding:**

* Protocol contained in the IPv4 packet: `[Add protocol]`
* Time to Live value: `[Add TTL]`
* Source IP address: `[Add source IP]`
* Destination IP address: `[Add destination IP]`

### 4. TCP Packet Analysis

I examined the TCP information to identify the source port, destination port, sequence information, and TCP flags.

**Finding:**

* Source port: `[Add source port]`
* Destination port: `[Add destination port]`
* TCP flags observed: `[Add flags]`
* What the ports or flags indicated: `[Explain your interpretation]`

### 5. DNS Traffic Analysis

I used the following filter to isolate DNS traffic:

```text
udp.port == 53
```

I inspected the DNS query and its corresponding response.

**Finding:**

* Domain queried: `[Add domain]`
* DNS server or destination: `[Add address if observed]`
* IP address returned: `[Add returned IP address]`
* What this traffic demonstrated: `[Explain the query-and-response process]`

### 6. HTTP Content Analysis

I searched TCP packets for traffic containing the text `curl`:

```text
tcp contains "curl"
```

**Finding:**
[Describe the packets returned and what the visible payload information suggested.]

## Summary of Findings

| Finding                     | Result          |
| --------------------------- | --------------- |
| Ping protocol               | `[Add result]`  |
| Primary IP address examined | `142.250.1.139` |
| TCP destination port        | `[Add port]`    |
| DNS port                    | `53`            |
| Web traffic port            | `[Add port]`    |
| Domain queried              | `[Add domain]`  |
| Returned IP address         | `[Add address]` |
| TCP flags observed          | `[Add flags]`   |

## Security Analysis

The investigation demonstrated how packet analysis can reveal the systems communicating on a network, the protocols and ports being used, and the sequence of events involved in accessing a website.

[Add two or three sentences explaining whether the traffic appeared normal or suspicious and what evidence supported your conclusion.]

## Evidence

Screenshots will be added after the lab is completed and all images have been checked for sensitive information.

* Unfiltered packet overview
* IP address filter
* TCP packet details
* DNS query
* DNS response
* TCP packets containing `curl`

## What I Learned

This project strengthened my ability to navigate Wireshark, apply targeted display filters, inspect packet headers, and explain network activity using evidence from a packet capture.

[Add one personal sentence about what was difficult, surprising, or especially useful.]

## Ethical and Privacy Notice

This project was completed in an authorized training environment. The scenario and network data are fictional or provided specifically for educational use. No private credentials, personal information, or unauthorized network traffic are included.
