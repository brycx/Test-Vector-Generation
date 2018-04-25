## PBKDF2 HMAC-SHA2 Test Vectors

These are test vectors for PBKDF2 with SHA256, SHA384 and SHA512. Input parameters P, S, c and dkLen are
consistent with those from the [RFC 6070](https://tools.ietf.org/html/rfc6070).

The following test vectors have been generated with the Python [cryptography](https://cryptography.io/en/latest/) package.
This package has been [tested](https://cryptography.io/en/latest/development/test-vectors/)
with the original test vectors from [RFC 6070](https://tools.ietf.org/html/rfc6070).


#### Test Case 1
```
     Input:
       P = "password" (8 octets)
       S = "salt" (4 octets)
       c = 1
       dkLen = 20

     Output:
       PBKDF2-HMAC-SHA256 = 120fb6cffcf8b32c43e7225256c4f837a86548c9 (20 octets)

       PBKDF2-HMAC-SHA384 = c0e14f06e49e32d73f9f52ddf1d0c5c719160923 (20 octets)

       PBKDF2-HMAC-SHA512 = 867f70cf1ade02cff3752599a3a53dc4af34c7a6 (20 octets)

```
#### Test Case 2
```
     Input:
       P = "password" (8 octets)
       S = "salt" (4 octets)
       c = 2
       dkLen = 20

     Output:
       PBKDF2-HMAC-SHA256 = ae4d0c95af6b46d32d0adff928f06dd02a303f8e (20 octets)

       PBKDF2-HMAC-SHA384 = 54f775c6d790f21930459162fc535dbf04a93918 (20 octets)

       PBKDF2-HMAC-SHA512 = e1d9c16aa681708a45f5c7c4e215ceb66e011a2e (20 octets)

```
#### Test Case 3
```
     Input:
       P = "password" (8 octets)
       S = "salt" (4 octets)
       c = 4096
       dkLen = 20

     Output:
       PBKDF2-HMAC-SHA256 = c5e478d59288c841aa530db6845c4c8d962893a0 (20 octets)

       PBKDF2-HMAC-SHA384 = 559726be38db125bc85ed7895f6e3cf574c7a01c (20 octets)

       PBKDF2-HMAC-SHA512 = d197b1b33db0143e018b12f3d1d1479e6cdebdcc (20 octets)
```
#### Test Case 4
```
     Input:
       P = "password" (8 octets)
       S = "salt" (4 octets)
       c = 16777216
       dkLen = 20

     Output:
       PBKDF2-HMAC-SHA256 = cf81c66fe8cfc04d1f31ecb65dab4089f7f179e8 (20 octets)

       PBKDF2-HMAC-SHA384 = a7fdb349ba2bfa6bf647bb0161bae1320df27e64 (20 octets)

       PBKDF2-HMAC-SHA512 = 6180a3ceabab45cc3964112c811e0131bca93a35 (20 octets)

```
#### Test Case 5
```
     Input:
       P = "passwordPASSWORDpassword" (24 octets)
       S = "saltSALTsaltSALTsaltSALTsaltSALTsalt" (36 octets)
       c = 4096
       dkLen = 25

     Output:
       PBKDF2-HMAC-SHA256 = 348c89dbcbd32b2f32d814b8116e84cf2b17347ebc1800181c (25 octets)

       PBKDF2-HMAC-SHA384 = 819143ad66df9a552559b9e131c52ae6c5c1b0eed18f4d283b (25 octets)

       PBKDF2-HMAC-SHA512 = 8c0511f4c6e597c6ac6315d8f0362e225f3c501495ba23b868 (25 octets)
```
#### Test Case 6
```
     Input:
       P = "pass\0word" (9 octets)
       S = "sa\0lt" (5 octets)
       c = 4096
       dkLen = 16

     Output:
       PBKDF2-HMAC-SHA256 = 89b69d0516f829893c696226650a8687 (16 octets)

       PBKDF2-HMAC-SHA384 = a3f00ac8657e095f8e0823d232fc60b3 (16 octets)

       PBKDF2-HMAC-SHA512 = 9d9e9c4cd21fe4be24d5b8244c759665 (16 octets)
```
