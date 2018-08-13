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

#### Test Case 7
```
     Input:
       P = "passwd"
       S = "salt"
       c = 1
       dkLen = 128

     Output:
       PBKDF2-HMAC-SHA256 = "55ac046e56e3089fec1691c22544b605f94185216dde0465e68b9d57c20dacbc49ca9cccf179b645991664b39d77ef317c71b845b1e30bd509112041d3a19783c294e850150390e1160c34d62e9665d659ae49d314510fc98274cc79681968104b8f89237e69b2d549111868658be62f59bd715cac44a1147ed5317c9bae6b2a"

       PBKDF2-HMAC-SHA384 = "cd3443723a41cf1460cca9efeede428a8898a82d2ad4d1fc5cca08ed3f4d3cb47a62a70b3cb9ce65dcbfb9fb9d425027a8be69b53e2a22674b0939e5e0a682f76d21f449ad184562a3bc4c519b4d048de6d8e0999fb88770f95e40185e19fc8b68767417ccc064f47a455d045b3bafda7e81b97ad0e4c5581af1aa27871cd5e4"

       PBKDF2-HMAC-SHA512 = "c74319d99499fc3e9013acff597c23c5baf0a0bec5634c46b8352b793e324723d55caa76b2b25c43402dcfdc06cdcf66f95b7d0429420b39520006749c51a04ef3eb99e576617395a178ba33214793e48045132928a9e9bf2661769fdc668f31798597aaf6da70dd996a81019726084d70f152baed8aafe2227c07636c6ddece"
```

#### Test Case 8
```
     Input:
       P = "Password"
       S = "NaCl"
       c = 80000
       dkLen = 128

     Output:
       PBKDF2-HMAC-SHA256 = "4ddcd8f60b98be21830cee5ef22701f9641a4418d04c0414aeff08876b34ab56a1d425a1225833549adb841b51c9b3176a272bdebba1d078478f62b397f33c8d62aae85a11cdde829d89cb6ffd1ab0e63a981f8747d2f2f9fe5874165c83c168d2eed1d2d5ca4052dec2be5715623da019b8c0ec87dc36aa751c38f9893d15c3"

       PBKDF2-HMAC-SHA384 = "11c198987730fa113458053cd5cc9b51d7024a35f9134f1ee8740923c901aab23bbaea43686981b6e6a9f4130a1401daeeec74060246ebac958f3cfc3c65579b6e3d08b94ade5fc257a6902a0a1664b8dbd5a8ae2af70438931d3f3679abffc7a17770582f1ee413cc0d9914ce5f8143c8a7dc9c43fbc31e3d41b2030fb73c02"

       PBKDF2-HMAC-SHA512 = "e6337d6fbeb645c794d4a9b5b75b7b30dac9ac50376a91df1f4460f6060d5addb2c1fd1f84409abacc67de7eb4056e6bb06c2d82c3ef4ccd1bded0f675ed97c65c33d39f81248454327aa6d03fd049fc5cbb2b5e6dac08e8ace996cdc960b1bd4530b7e754773d75f67a733fdb99baf6470e42ffcb753c15c352d4800fb6f9d6"
```
