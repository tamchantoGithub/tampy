import base64

encoded="Hello".encode()
print(encoded)

base64_encoded=base64.b64encode(encoded)
print(base64_encoded)