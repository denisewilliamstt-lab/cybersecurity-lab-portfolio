# Linux Cryptography and File Decryption

## Project Overview

This project demonstrates how Linux command-line tools can be used to locate hidden files, decode a Caesar cipher, and decrypt an encrypted data file. The work was completed in a controlled Linux virtual machine while logged in as the `analyst` user.

The exercise combined basic Bash navigation with two different cryptographic concepts:

- **Substitution decoding:** Reversing a Caesar shift with `tr`.
- **Symmetric decryption:** Recovering a file protected with AES-256-CBC by using OpenSSL and a password-derived key.

## Scenario

Files in the analyst's home directory had been encrypted. A visible README provided the first clue, and a hidden file in a subdirectory contained a Caesar-cipher message. Decoding that message revealed the OpenSSL command needed to recover the encrypted data.

## Environment

| Component | Details |
|---|---|
| Operating environment | Linux virtual machine |
| Shell | Bash |
| User | `analyst` |
| Starting directory | `/home/analyst` |
| Tools | `ls`, `cd`, `cat`, `tr`, OpenSSL |
| Encrypted input | `Q1.encrypted` |
| Recovered output | `Q1.recovered` |

## Objectives

- Inspect files in the home directory.
- Read instructions stored in a text file.
- Locate a hidden Linux file.
- Reverse a Caesar cipher with character translation.
- Use OpenSSL to decrypt an AES-256-CBC protected file.
- Confirm that the recovered file was created and readable.

## Command Summary

| Command | Purpose |
|---|---|
| `ls` | List visible files and directories. |
| `cat README.txt` | Read the initial instructions. |
| `cd caesar` | Enter the Caesar-cipher subdirectory. |
| `ls -a` | Display all entries, including hidden files. |
| `cat .leftShift3` | Display the Caesar-cipher text. |
| `cat .leftShift3 \| tr "d-za-cD-ZA-C" "a-zA-Z"` | Translate shifted characters back to the standard alphabet. |
| `cd ~` | Return to the analyst's home directory. |
| `openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute` | Decrypt the protected input and write the recovered plaintext to a new file. |
| `cat Q1.recovered` | Read the recovered message. |

## Procedure and Results

### 1. Inspected the home directory

I listed the current directory:

```bash
ls
```

The output showed:

```text
Q1.encrypted
README.txt
caesar/
```

I read the instruction file:

```bash
cat README.txt
```

The message directed me to search the `caesar` subdirectory for a hidden file.

### 2. Located the hidden clue

I entered the subdirectory and listed all entries:

```bash
cd caesar
ls -a
```

The `-a` option was necessary because Linux filenames beginning with a period are hidden from a standard `ls` listing. The output revealed `.leftShift3`.

I displayed its encrypted contents:

```bash
cat .leftShift3
```

The text was unreadable because each alphabetical character had been shifted three positions.

### 3. Reversed the Caesar shift

I piped the hidden file's contents into `tr`:

```bash
cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"
```

The pipe (`|`) sent the output from `cat` to the input of `tr`. The first character set represented the shifted alphabet, while the second represented the normal lowercase and uppercase alphabet. The decoded message revealed the command required to decrypt the main file.

### 4. Decrypted the protected file

I returned to the home directory:

```bash
cd ~
```

I then used OpenSSL to recover the data:

```bash
openssl aes-256-cbc -pbkdf2 -a -d \
  -in Q1.encrypted \
  -out Q1.recovered \
  -k ettubrute
```

### 5. Verified the result

I confirmed that a new file had been created:

```bash
ls
```

The directory now included `Q1.recovered`. I displayed the recovered plaintext:

```bash
cat Q1.recovered
```

The readable output confirmed that the decryption process succeeded.

## OpenSSL Command Breakdown

| Option | Meaning |
|---|---|
| `aes-256-cbc` | Uses the AES algorithm with a 256-bit key in Cipher Block Chaining mode. |
| `-pbkdf2` | Derives the encryption key from the password using PBKDF2. |
| `-a` | Indicates that the encrypted input uses Base64 encoding. |
| `-d` | Selects decryption rather than encryption. |
| `-in Q1.encrypted` | Identifies the encrypted source file. |
| `-out Q1.recovered` | Specifies the recovered plaintext output file. |
| `-k ettubrute` | Supplies the password used for key derivation in this training scenario. |

## Cryptographic Analysis

### Caesar cipher

The Caesar cipher substitutes each letter with another letter at a fixed offset. It is useful for learning the concept of substitution, but it is not secure for protecting real information. The keyspace is extremely small, letter patterns remain visible, and an attacker can test every possible shift quickly.

### AES-256-CBC

AES is a modern symmetric encryption algorithm, meaning the same secret is used to encrypt and decrypt data. CBC mode also requires correct initialization-vector and padding handling. OpenSSL manages those details in this exercise.

### PBKDF2

A human password is not used directly as an AES key. PBKDF2 repeatedly processes the password with a salt to derive stronger key material and make password guessing more expensive. In production, passwords should be provided securely through a prompt or protected secret-management process rather than placed directly in command history.

### Base64

Base64 is an encoding method, not encryption. It converts binary data into text characters for storage or transmission, but anyone can reverse it without a secret.

## Security Considerations

- Avoid placing passwords directly on the command line because they may appear in shell history or process information.
- Restrict permissions on encrypted files, recovered plaintext, and cryptographic keys.
- Use strong, unique secrets and an approved secret manager.
- Prefer authenticated-encryption modes in modern production designs so unauthorized changes can be detected.
- Verify recovered files before deleting the encrypted originals.
- Keep sensitive plaintext only as long as business requirements demand.

## Key Takeaways

- `ls -a` reveals files intentionally hidden from ordinary directory listings.
- Pipes allow Linux commands to work together without creating unnecessary intermediate files.
- Simple substitution ciphers do not provide meaningful modern security.
- Encryption and encoding solve different problems and should not be confused.
- Successful decryption should be verified by confirming the output file and reviewing its contents.
- Cryptographic security depends on algorithms, configuration, key derivation, and secret handling—not merely on running an encryption command.

## Skills Demonstrated

- Linux file and directory navigation
- Hidden-file discovery
- Bash pipes and text translation
- Caesar-cipher decoding
- OpenSSL file decryption
- AES and PBKDF2 concept analysis
- Output verification
- Secure command-line practices
- Technical documentation

## Project Note

This portfolio project is based on a guided cybersecurity lab completed in a controlled training environment. The documentation and security analysis were prepared as an original professional summary of the work performed.
