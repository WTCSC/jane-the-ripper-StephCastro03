[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21523143)
# README - Jane the Ripper

## DESCRIPTION:
- Small Python utility that attempts to match MD5 hashes to plaintext candidates from a supplied wordlist. Reads target MD5 hex digests from a file and prints cracked results (supports multiple plaintexts per hash).

## REQUIREMENTS:
- Python 3

## FILES / USAGE (examples):
This script expects:
- wordlist: newline-separated plaintext candidates (one per line)
- hashes: newline-separated MD5 hex digests (one per line)
## Interactive:
Run the main script and follow prompts:
python3 jane_the_ripper.py
Prompts:
- Enter path to hash file:
- Enter path to wordlist file:

## Non-interactive (suggested modification shown below):
python3 jane_the_ripper.py --hashes hashes.txt --wordlist wordlist.txt

## EXAMPLE FORMATS:
Wordlist file (wordlist.txt):
- password123
- letmein
- abc123
- 123456

## Hash file (hashes.txt):
-  e10adc3949ba59abbe56e057f20f883e
-  482c811da5d5b4bc6d497ffa98491e38
-   00000000000000000000000000000000

## OUTPUT EXAMPLES:
- [+] Cracked: e10adc3949ba59abbe56e057f20f883e  -->  123456
- [-] Failed: 00000000000000000000000000000000  -->  Password not found in the wordlist
- [!] Some hashes were not found in the wordlist provided

How it Runs
