# Linux Software Management with APT

## Project Overview

This project demonstrates how to manage security applications from a Linux Bash shell using the Advanced Package Tool (`apt`) and elevated privileges with `sudo`. The work was completed in a Debian-based virtual machine to provide a controlled environment for installing, removing, and validating software.

The exercise focused on two common network-security tools:

- **Suricata:** An intrusion detection and network analysis application.
- **tcpdump:** A command-line packet-capture and traffic-analysis utility.

## Scenario

As a security analyst, I needed to prepare a Linux system with Suricata and tcpdump. I verified that the required package manager was available, installed and removed Suricata, installed tcpdump, reviewed the system's installed packages, and then restored Suricata. Each major change was validated from the command line.

## Environment

| Component | Details |
|---|---|
| Operating system | Debian-based Linux distribution |
| Interface | Bash shell |
| User account | `analyst` |
| Package manager | APT |
| Privilege elevation | `sudo` |
| Execution environment | Virtual machine |

## Objectives

- Confirm that APT is available.
- Install and verify Suricata.
- Remove Suricata and verify its removal.
- Install tcpdump.
- Review the installed-package list.
- Reinstall Suricata and confirm that both security tools are present.

## Command Summary

| Command | Purpose |
|---|---|
| `apt` | Confirm that APT is installed and display its usage information. |
| `sudo apt install suricata` | Install Suricata and its required dependencies. |
| `suricata` | Run Suricata to verify that the executable is available. |
| `sudo apt remove suricata` | Remove the Suricata package. |
| `sudo apt install tcpdump` | Install tcpdump. |
| `apt list --installed` | Display packages currently installed on the system. |

## Procedure and Results

### 1. Verified the package manager

I checked whether APT was available:

```bash
apt
```

APT returned version and usage information, confirming that the Debian package manager was installed and ready for use.

### 2. Installed Suricata

I installed Suricata with administrative privileges:

```bash
sudo apt install suricata
```

APT identified the package and its dependencies, requested confirmation, and completed the installation.

I then verified the installation:

```bash
suricata
```

Suricata returned version and usage information, demonstrating that the executable was installed successfully.

### 3. Removed and validated the removal of Suricata

I removed the application:

```bash
sudo apt remove suricata
```

I tested the command again after removal:

```bash
suricata
```

The shell returned a command-not-found error. This confirmed that the Suricata executable was no longer available.

### 4. Installed tcpdump

I installed the packet-capture utility:

```bash
sudo apt install tcpdump
```

The package manager completed the installation and made tcpdump available on the system.

### 5. Reviewed installed applications

I listed the installed packages:

```bash
apt list --installed
```

The output included tcpdump but did not include Suricata, which matched the expected system state after Suricata had been removed.

### 6. Restored Suricata and completed final verification

I reinstalled Suricata:

```bash
sudo apt install suricata
```

I listed the packages again:

```bash
apt list --installed
```

The final package list confirmed that both Suricata and tcpdump were installed.

## Final System State

| Application | Final Status | Security Use |
|---|---|---|
| Suricata | Installed | Network monitoring and intrusion detection |
| tcpdump | Installed | Command-line packet capture and traffic inspection |

## Security Significance

Package management is an important administrative and security responsibility. Analysts must be able to deploy approved tools, remove unnecessary or vulnerable software, confirm the state of a system, and use elevated privileges carefully. Validating each change also reduces the chance of assuming that an installation or removal succeeded when it did not.

Using a virtual machine created a safer testing environment and allowed the system to be restored if a command caused an unwanted change.

## Key Takeaways

- APT simplifies software and dependency management on Debian-based systems.
- Installing or removing software requires elevated privileges, which should be used only when necessary.
- Successful package-manager output should be followed by an independent verification step.
- Installed-package inventories help analysts understand the tools and potential attack surface present on a system.
- Suricata and tcpdump support different but complementary network-security workflows.

## Skills Demonstrated

- Linux command-line administration
- Debian package management with APT
- Safe use of `sudo`
- Software installation and removal
- System-state validation
- Security-tool deployment
- Technical documentation

## Project Note

This portfolio project is based on a guided cybersecurity lab completed in a fictional training environment. The documentation and analysis were written as an original professional summary of the work performed.
