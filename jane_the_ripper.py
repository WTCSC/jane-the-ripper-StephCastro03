import hashlib
import os
from collections import defaultdict

def ask_file_path(prompt):
    while True:
        path = input(prompt).strip()
        if os.path.isfile(path):
            return path
        else:
            print("File not found. Please try again.")
def building_mapping(wordlist_path):
    mapping = defaultdict(list)
    with open (wordlist_path, 'r') as f:
        for line in f:
            password = line.strip()
            if not password:
                continue
            md5_hash = hashlib.md5(password.encode()).hexdigest()
            mapping[md5_hash].append(password)
            return mapping
def crack_passwords(hash_path, wordlist_path):
    with open (hash_path, 'r') as f:
       targets = {line.strip() for line in f if line.strip()}
    mapping = building_mapping(wordlist_path)
    return {t: mapping[t] if t in mapping else ['Password not found in the wordlist'] for t in targets}
def run_basic_test():
    wordlist_file_path, hash_file_path = "test_wordlist.txt", "test_hashes.txt"
    sample_passwords = ["password123", "letmein", "abc123", "123456"]
    with open(wordlist_file_path, 'w') as wordlist_handle:
        for password in sample_passwords:
            wordlist_handle.write(password + '\n')
    with open(hash_file_path, 'w') as hashes_handles:
        for password in ("123456", "password"):
            hashes_handles.write(hashlib.md5(password.encode('utf-8')).hexdigest() + '\n')
        hashes_handles.write("0000000000000000000000000000000000\n")
        results = crack_passwords(hash_file_path, wordlist_file_path)
        for has_value, plaintexts in results.items():
            if plaintexts and plaintexts[0] != 'Password not found in the wordlist':
                for plaintext in plaintexts:
                    print(f"[+] Cracked: {has_value}  -->  {plaintext}")
            else:
                print(f"[-] Failed: {has_value}  -->  Password not found in the wordlist")
        os.remove(wordlist_file_path)
        os.remove(hash_file_path)

    def main():
        print("Welcome to Jane the Ripper- password cracker!")
        hash_file_path = ask_file_path("Enter path to hase file: ")
        wordlist_file_path = ask_file_path("Enter path to wordlist file:")
        results = crack_passwords(hash_file_path, wordlist_file_path)
        all_cracked = True
        for hash_value, plaintexts in results.items():
            if plaintexts and plaintexts[0] != 'Password not found in the wordlist':
                for plaintext in plaintexts:
                    print(f"[+] Cracked: {hash_value}  -->  {plaintext}")
            else:
                all_cracked = False
                print(f"[-] Failed: {hash_value}  -->  Password not found in the wordlist")
        print("[!] All hashes were cracked successfully!" if all_cracked else "[!] Some hases were not found in the wordlist provided")
        if input("Run basic test? (y/n): ").strip().lower() == 'y':
            run_basic_test()
    if __name__ == "__main__":
        main()
