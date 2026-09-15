# README

# Wireshark Network Traffic Analysis

## Project Overview

In this project, I acted as a security analyst investigating network traffic generated when a user connected to a website. I used Wireshark to examine a packet capture (`.pcap`) file, apply display filters, inspect network protocol layers, and identify relevant ICMP, DNS, TCP, and HTTP traffic.

## Objectives

- Identify source and destination IP addresses involved in the browsing session.
- Examine Ethernet, IPv4, TCP, UDP, DNS, HTTP, and ICMP traffic.
- Filter packets by IP address, MAC address, port, and payload text.
- Inspect packet headers, protocol fields, and TCP flags.
- Interpret the connection activity shown in the packet capture.

## Tools and Skills

- Wireshark
- Packet capture analysis
- Display filters
- TCP/IP and UDP
- DNS and HTTP analysis
- ICMP analysis
- Ethernet and MAC addressing

## Investigation

### 1. Initial Packet Review

I opened the sample packet capture and reviewed Wireshark’s packet list, packet details, and raw packet bytes. The unfiltered capture contained 200 packets and included SSH, TCP, DNS, ICMP, and HTTP traffic.

Unfiltered Wireshark packet capture

!Unfiltered Wireshark packet capture

Unfiltered Wireshark packet capture

### 2. ICMP Echo Traffic

I located the first packet whose Info field began with `Echo (ping) request`. Packet 16 used ICMP and traveled from `172.21.224.2` to `142.250.1.139`. This traffic represents a connectivity test sent to the destination system.

ICMP Echo request

!ICMP Echo request

ICMP Echo request

### 3. IP Address Filtering

I applied the following display filter:

```
ip.addr == 142.250.1.139
```

This reduced the packet list to traffic where `142.250.1.139` appeared as either the source or destination. The filtered results included ICMP, TCP, and HTTP packets.

Traffic filtered by IP address

!Traffic filtered by IP address

Traffic filtered by IP address

I also practiced directional filtering:

```
ip.src == 142.250.1.139
ip.dst == 142.250.1.139
```

The `ip.src` filter isolates packets sent from the address, while `ip.dst` isolates packets sent to it.

### 4. TCP Connection Analysis

I inspected the first TCP packet in the filtered results and identified these fields:

| Field | Value |
| --- | --- |
| Source MAC | `42:01:ac:15:e0:02` |
| Destination MAC | `42:01:ac:15:e0:01` |
| Source IP | `172.21.224.2` |
| Destination IP | `142.250.1.139` |
| Source port | `49652` |
| Destination port | `80` |
| TCP flags | `0x002 (SYN)` |

TCP packet summary

!TCP packet summary

TCP packet summary

The client used temporary source port `49652` to contact destination port `80`, which is associated with HTTP. The SYN flag indicates the client was initiating a TCP connection—the first step of the TCP three-way handshake.

TCP SYN flag details

!TCP SYN flag details

TCP SYN flag details

### 5. MAC Address and IPv4 Filtering

I filtered traffic involving a specific Ethernet address:

```
eth.addr == 42:01:ac:15:e0:02
```

The selected packet showed `42:01:ac:15:e0:02` as the source MAC address. Its IPv4 header showed source IP `172.21.224.2`, destination IP `142.250.1.139`, a Time to Live of 64, and ICMP as the encapsulated protocol.

MAC address filter and IPv4 details

!MAC address filter and IPv4 details

MAC address filter and IPv4 details

### 6. DNS Analysis

I isolated DNS traffic with:

```
udp.port == 53
```

The DNS query requested `opensource.google.com`, and the DNS answer associated the name with IP address `142.250.1.139`.

### 7. TCP and Payload Analysis

I isolated web traffic on TCP port 80:

```
tcp.port == 80
```

One inspected packet had a Time to Live of 64, a frame length of 54 bytes, an IPv4 header length of 20 bytes, and destination address `169.254.169.254`.

I then searched TCP payload data for traffic containing the text `curl`:

```
tcp contains "curl"
```

This identified packets containing web requests made with the curl command-line tool.

## Key Findings

- The client at `172.21.224.2` communicated with `142.250.1.139` using ICMP, TCP, and HTTP-related traffic.
- ICMP Echo request and reply packets demonstrated a connectivity check between the systems.
- DNS traffic resolved `opensource.google.com` to `142.250.1.139`.
- A TCP SYN packet from source port `49652` to destination port `80` showed the beginning of a web connection.
- Wireshark display filters efficiently isolated traffic by IP address, MAC address, protocol port, and packet contents.

## Security Analysis

Packet analysis provides visibility into which systems communicate, which protocols and ports they use, and how connections begin. Filters help analysts reduce large captures to the traffic relevant to an investigation. In a real environment, HTTP traffic on port 80 deserves attention because it is normally unencrypted, which may allow transmitted content to be inspected if encryption is not applied at another layer.

## Lessons Learned

This project strengthened my ability to navigate Wireshark, interpret layered packet data, distinguish source and destination fields, analyze a TCP SYN packet, examine DNS resolution, and build focused display filters. I also practiced connecting low-level packet fields to the larger story of a web-browsing session.

## Evidence Note

The screenshots and addresses in this project come from a controlled training environment. No production systems or personal data were analyzed.
