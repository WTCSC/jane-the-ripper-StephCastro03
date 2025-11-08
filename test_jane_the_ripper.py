import os 
import hashlib
import jane_the_ripper as jtr

def md5_hex(s):
    return hashlib.md5(s.encode()).hexdigest()
wordlist_file = "test_wordlist.txt"
hash_file = "test_hashes.txt"

with open(wordlist_file, 'w') as f:
    f.write("123456\npassword\n")
with open(hash_file, "w") as f:
    f.write(md5_hex("123456") + "\n")
    f.write(md5_hex("password") + "\n")
    f.write("0"*32 + "\n")
print("Testing building_mapping...")
mapping = jtr.building_mapping(wordlist_file)
if md5_hex("123456") in mapping and "123456" in mapping[md5_hex("123456")]:
    print("PASS: 123456 mapped correctly")
else:
    print("FAIL: 123456 mapping missing")
if md5_hex("password") in mapping and "password" in mapping[md5_hex("password")]:
    print("PASS: password mapped correctly")
else:
    print("FAIL: password mapping missing")
print("Testing crack_passwords...")
results = jtr.crack_passwords(hash_file, wordlist_file)
for h in [md5_hex("123456"), md5_hex("password"), "0"*32]:
    if h in results:
        print(f"Hash: {h}")
        print(f"  Result: {results[h]}")
    else:
        print(f"FAIL: Hash {h} not in results")

os.remove(wordlist_file)
os.remove(hash_file)
