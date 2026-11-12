# Wireshark Display Filters Used

| Purpose | Filter |
|---|---|
| Initial TCP SYN requests | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| TCP SYN-ACK responses | `tcp.flags.syn == 1 && tcp.flags.ack == 1` |
| TCP reset packets | `tcp.flags.reset == 1` |
| Initial SYN traffic involving suspected scanner | `ip.addr == 198.51.100.77 && tcp.flags.syn == 1 && tcp.flags.ack == 0` |

## Important interpretation
- A SYN indicates an attempt to start a TCP connection, not a completed connection.
- A SYN-ACK indicates a response, not proof that the final ACK or application exchange occurred.
- RST can indicate refusal or termination; correlate the 4-tuple and sequence to interpret.
- Wireshark Conversations counts may change when **Limit to display filter** is enabled.
