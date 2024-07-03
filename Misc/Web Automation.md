In one of the commits, I found the secret key in the `.env` file.

<figure><img src="../src/Misc/Web Automation/commit.png"></figure>

On decoding it with `base64`, I got the flag.

<figure><img src="../src/Misc/Web Automation/flag.png"></figure>

Flag:
```
ThunderCipher{S3cr3T_1N_G1t_C0mMit!===}
```