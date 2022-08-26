import os
import binascii

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend

backend = default_backend()

test_vector_1_224 = HKDF (
    algorithm = hashes.SHA224(),
    length = 32,
    salt = binascii.unhexlify("000102030405060708090a0b0c"),
    info = b"",
    backend = backend
)

test_vector_2_224 = HKDF (
    algorithm = hashes.SHA224(),
    length = 128,
    salt = b"salt",
    info = b"random InF\0",
    backend = backend
)

test_vector_3_224 = HKDF (
    algorithm = hashes.SHA224(),
    length = 256,
    salt = binascii.unhexlify("606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeaf"),
    info = b"",
    backend = backend
)

test_vector_4_224 = HKDF (
    algorithm = hashes.SHA224(),
    length = 256,
    salt = b"s$#$#%$#SBGHWE@#W#lt",
    info = b"random InF\0",
    backend = backend
)

test_vector_5_224 = HKDF (
    algorithm = hashes.SHA224(),
    length = 32,
    salt = b"salt",
    info = b"",
    backend = backend
)

test_vector_6_224 = HKDF (
    algorithm = hashes.SHA224(),
    length = 16,
    salt = b"saltSALTSALTSALTSALTSALTSALTSALTSALTSALTSALTSALTSALT",
    info = binascii.unhexlify("b0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"),
    backend = backend
)
###############################################################################
test_vector_1_256 = HKDF (
    algorithm = hashes.SHA256(),
    length = 32,
    salt = binascii.unhexlify("000102030405060708090a0b0c"),
    info = b"",
    backend = backend
)

test_vector_2_256 = HKDF (
    algorithm = hashes.SHA256(),
    length = 128,
    salt = b"salt",
    info = b"random InF\0",
    backend = backend
)

test_vector_3_256 = HKDF (
    algorithm = hashes.SHA256(),
    length = 256,
    salt = binascii.unhexlify("606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeaf"),
    info = b"",
    backend = backend
)

test_vector_4_256 = HKDF (
    algorithm = hashes.SHA256(),
    length = 256,
    salt = b"s$#$#%$#SBGHWE@#W#lt",
    info = b"random InF\0",
    backend = backend
)

test_vector_5_256 = HKDF (
    algorithm = hashes.SHA256(),
    length = 32,
    salt = b"salt",
    info = b"",
    backend = backend
)

test_vector_6_256 = HKDF (
    algorithm = hashes.SHA256(),
    length = 16,
    salt = b"saltSALTSALTSALTSALTSALTSALTSALTSALTSALTSALTSALTSALT",
    info = binascii.unhexlify("b0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"),
    backend = backend
)
###############################################################################
test_vector_1_384 = HKDF (
    algorithm = hashes.SHA384(),
    length = 32,
    salt = binascii.unhexlify("000102030405060708090a0b0c"),
    info = b"",
    backend = backend
)

test_vector_2_384 = HKDF (
    algorithm = hashes.SHA384(),
    length = 128,
    salt = b"salt",
    info = b"random InF\0",
    backend = backend
)

test_vector_3_384 = HKDF (
    algorithm = hashes.SHA384(),
    length = 256,
    salt = binascii.unhexlify("606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeaf"),
    info = b"",
    backend = backend
)

test_vector_4_384 = HKDF (
    algorithm = hashes.SHA384(),
    length = 256,
    salt = b"s$#$#%$#SBGHWE@#W#lt",
    info = b"random InF\0",
    backend = backend
)

test_vector_5_384 = HKDF (
    algorithm = hashes.SHA384(),
    length = 32,
    salt = b"salt",
    info = b"",
    backend = backend
)

test_vector_6_384 = HKDF (
    algorithm = hashes.SHA384(),
    length = 16,
    salt = b"saltSALTSALTSALTSALTSALTSALTSALTSALTSALTSALTSALTSALT",
    info = binascii.unhexlify("b0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"),
    backend = backend
)
###############################################################################
test_vector_1_512 = HKDF (
    algorithm = hashes.SHA512(),
    length = 32,
    salt = binascii.unhexlify("000102030405060708090a0b0c"),
    info = b"",
    backend = backend
)

test_vector_2_512 = HKDF (
    algorithm = hashes.SHA512(),
    length = 128,
    salt = b"salt",
    info = b"random InF\0",
    backend = backend
)

test_vector_3_512 = HKDF (
    algorithm = hashes.SHA512(),
    length = 256,
    salt = binascii.unhexlify("606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeaf"),
    info = b"",
    backend = backend
)

test_vector_4_512 = HKDF (
    algorithm = hashes.SHA512(),
    length = 256,
    salt = b"s$#$#%$#SBGHWE@#W#lt",
    info = b"random InF\0",
    backend = backend
)

test_vector_5_512 = HKDF (
    algorithm = hashes.SHA512(),
    length = 32,
    salt = b"salt",
    info = b"",
    backend = backend
)

test_vector_6_512 = HKDF (
    algorithm = hashes.SHA512(),
    length = 16,
    salt = b"saltSALTSALTSALTSALTSALTSALTSALTSALTSALTSALTSALTSALT",
    info = binascii.unhexlify("b0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"),
    backend = backend
)
###############################################################################
print("SHA224 TC1:", binascii.hexlify(test_vector_1_224.derive(binascii.unhexlify("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"))))
print("SHA224 TC2:", binascii.hexlify(test_vector_2_224.derive(binascii.unhexlify("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f"))))
print("SHA224 TC3:", binascii.hexlify(test_vector_3_224.derive(b"password")))
print("SHA224 TC4:", binascii.hexlify(test_vector_4_224.derive(binascii.unhexlify("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"))))
print("SHA224 TC5:", binascii.hexlify(test_vector_5_224.derive(b"passwordPASSWORDpassword")))
print("SHA224 TC6:", binascii.hexlify(test_vector_6_224.derive(b"pass\0word")))
###############################################################################
print("SHA256 TC1:", binascii.hexlify(test_vector_1_256.derive(binascii.unhexlify("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"))))
print("SHA256 TC2:", binascii.hexlify(test_vector_2_256.derive(binascii.unhexlify("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f"))))
print("SHA256 TC3:", binascii.hexlify(test_vector_3_256.derive(b"password")))
print("SHA256 TC4:", binascii.hexlify(test_vector_4_256.derive(binascii.unhexlify("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"))))
print("SHA256 TC5:", binascii.hexlify(test_vector_5_256.derive(b"passwordPASSWORDpassword")))
print("SHA256 TC6:", binascii.hexlify(test_vector_6_256.derive(b"pass\0word")))
###############################################################################
print("SHA384 TC1:", binascii.hexlify(test_vector_1_384.derive(binascii.unhexlify("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"))))
print("SHA384 TC2:", binascii.hexlify(test_vector_2_384.derive(binascii.unhexlify("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f"))))
print("SHA384 TC3:", binascii.hexlify(test_vector_3_384.derive(b"password")))
print("SHA384 TC4:", binascii.hexlify(test_vector_4_384.derive(binascii.unhexlify("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"))))
print("SHA384 TC5:", binascii.hexlify(test_vector_5_384.derive(b"passwordPASSWORDpassword")))
print("SHA384 TC6:", binascii.hexlify(test_vector_6_384.derive(b"pass\0word")))
###############################################################################
print("SHA512 TC1:", binascii.hexlify(test_vector_1_512.derive(binascii.unhexlify("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"))))
print("SHA512 TC2:", binascii.hexlify(test_vector_2_512.derive(binascii.unhexlify("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f"))))
print("SHA512 TC3:", binascii.hexlify(test_vector_3_512.derive(b"password")))
print("SHA512 TC4:", binascii.hexlify(test_vector_4_512.derive(binascii.unhexlify("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"))))
print("SHA512 TC5:", binascii.hexlify(test_vector_5_512.derive(b"passwordPASSWORDpassword")))
print("SHA512 TC6:", binascii.hexlify(test_vector_6_512.derive(b"pass\0word")))
