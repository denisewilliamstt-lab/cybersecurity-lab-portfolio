# Linux File Integrity Verification with SHA-256

## Project Overview

This project demonstrates how to validate file integrity in Linux by generating and comparing SHA-256 hash values. Two text files appeared identical when displayed in the terminal, but their cryptographic hashes proved that their underlying contents were different.

The exercise shows why security analysts should not rely only on filenames or visible text when validating a file. Even a subtle change—such as an invisible character, spacing difference, or modified byte—produces a substantially different digest.

## Scenario

I was asked to determine whether `file1.txt` and `file2.txt` were truly identical. I first inspected both files with `cat`, generated a SHA-256 digest for each, redirected those digests into separate files, and then used `cmp` to perform a byte-by-byte comparison.

## Environment

| Component | Details |
|---|---|
| Operating environment | Linux virtual machine |
| Shell | Bash |
| User | `analyst` |
| Starting directory | `/home/analyst` |
| Source files | `file1.txt`, `file2.txt` |
| Hash algorithm | SHA-256 |
| Tools | `ls`, `cat`, `sha256sum`, output redirection, `cmp` |

## Objectives

- Inspect two files from the command line.
- Generate a SHA-256 digest for each file.
- Determine whether apparently identical files contain the same bytes.
- Save hash output to separate files.
- Compare stored hashes byte by byte.
- Explain the security value and limitations of file hashing.

## Command Summary

| Command | Purpose |
|---|---|
| `ls` | List the files in the working directory. |
| `cat file1.txt` | Display the visible contents of the first file. |
| `cat file2.txt` | Display the visible contents of the second file. |
| `sha256sum file1.txt` | Calculate the first file's SHA-256 digest. |
| `sha256sum file2.txt` | Calculate the second file's SHA-256 digest. |
| `sha256sum file1.txt > file1hash` | Store the first digest in a new file. |
| `sha256sum file2.txt > file2hash` | Store the second digest in a new file. |
| `cat file1hash file2hash` | Display both stored hash records. |
| `cmp file1hash file2hash` | Compare the hash files byte by byte. |

## Procedure and Findings

### 1. Inspected the available files

I listed the home directory:

```bash
ls
```

The directory contained `file1.txt` and `file2.txt`.

### 2. Reviewed the visible file contents

I displayed both files:

```bash
cat file1.txt
cat file2.txt
```

The terminal output appeared identical. This visual inspection did not prove that the underlying byte sequences were the same because `cat` may not make differences such as whitespace, line endings, or non-printing characters obvious.

### 3. Generated SHA-256 digests

I calculated a digest for each source file:

```bash
sha256sum file1.txt
sha256sum file2.txt
```

The two commands produced different SHA-256 values. Because the digests did not match, the source files were not identical.

### 4. Saved the hash results

I redirected each command's output into a separate file:

```bash
sha256sum file1.txt > file1hash
sha256sum file2.txt > file2hash
```

The `>` operator created or replaced the destination file with the command output. Each result contained the calculated digest and its corresponding filename.

### 5. Displayed and compared the stored hashes

I reviewed both hash records:

```bash
cat file1hash file2hash
```

I then compared them byte by byte:

```bash
cmp file1hash file2hash
```

The comparison reported a difference at the first character of the first line. This confirmed that the hash values—and therefore the underlying source files—were different.

## Results Summary

| Validation Method | Observation | Conclusion |
|---|---|---|
| Visual inspection with `cat` | Text appeared identical. | Inconclusive |
| SHA-256 calculation | Digests were different. | Source files differ |
| Byte comparison with `cmp` | First difference occurred immediately in the stored hashes. | Hash records are not identical |

## Why the Hashes Changed Completely

Cryptographic hash functions are designed to exhibit the **avalanche effect**: a tiny change in input should produce a dramatically different output. This property helps analysts detect even very small file modifications.

A SHA-256 digest is:

- Deterministic: the same input produces the same digest.
- Fixed length: SHA-256 produces a 256-bit value regardless of file size.
- One-way: the original file cannot practically be reconstructed from the digest.
- Sensitive to changes: different file bytes should produce different values.

## Security Applications

Security teams use file hashes to:

- Validate downloaded software against a trusted publisher's digest.
- Detect unexpected changes to critical system files.
- Compare suspicious files with known malware indicators.
- Preserve evidence identifiers during incident response and digital forensics.
- Confirm that backups and transferred files remain intact.
- Identify duplicate or altered files during investigations.

## Security Limitations

A hash mismatch proves that two inputs differ, but a matching hash does not by itself prove that a file is trustworthy. An attacker may replace both a file and an unprotected checksum. Analysts should obtain expected hashes from authenticated, trusted sources or use digital signatures and message-authentication mechanisms where authenticity is required.

Hashes also reveal that a change occurred, but they do not identify what changed. Additional tools such as `diff`, hexadecimal viewers, metadata inspection, or forensic utilities may be needed to locate and explain the difference.

## Key Takeaways

- Files that look identical can contain different underlying bytes.
- SHA-256 provides a reliable fingerprint for integrity comparison.
- Shell redirection can preserve command output for later review.
- `cmp` identifies the location of the first byte-level difference.
- File integrity and file authenticity are related but separate security questions.
- Expected hash values must come from a trusted source.

## Skills Demonstrated

- Linux command-line navigation
- SHA-256 hash generation
- File-integrity validation
- Bash output redirection
- Byte-level file comparison
- Evidence interpretation
- Security-control analysis
- Technical documentation

## Project Note

This portfolio project is based on a guided cybersecurity lab completed in a controlled training environment. The documentation and security analysis were prepared as an original professional summary of the work performed.
