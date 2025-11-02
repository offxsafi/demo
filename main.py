import hashlib
print("Hashing methods")
print("1. SHA256")
print("2. MD5")
print("3. SHA384")
i = int(input("Enter hashing method:"))

if i==1:
    print("SHA256 hashing")
    i1 = input("Enter value for hashing:")
    h1 = hashlib.sha256(i1.encode())
    print(h1.hexdigest())
elif i==2:
    print("MD5 hashing")
    i2 = input("Enter value for hashing:")
    h2 = hashlib.md5(i2.encode())
    print(h2.hexdigest())
