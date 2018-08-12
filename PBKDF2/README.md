## PBKDF2-HMAC SHA2 test vectors
These are test vectors for the Password-Based Key Derivation Function 2 (PBKDF2), using HMAC with SHA256, SHA384 and SHA512.

All test vectors are located in ```pbkdf2-hmac-sha2-test-vectors.md```. The script
that was used to generate the test vector results, can be found in ```pbkdf2-sha2-test-vector-generation.py```.

Test vectors have been generated with the Python [cryptography](https://cryptography.io/en/latest/) package.
This package has been [tested](https://cryptography.io/en/latest/development/test-vectors/)
with the original test vectors from the [RFC 6070](https://tools.ietf.org/html/rfc6070).

These are **not official** test vectors, so if anyone happens to find these useful and
can confirm these test vectors on their machines, please open an issue and I will
add it somewhere.
