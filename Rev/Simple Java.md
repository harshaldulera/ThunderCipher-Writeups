On decompiling the `simple.class` file, I found a set of numbers that are converted to ascii by substracting by 7 and dividing by 10.

Wrote a script to get the flag.

```
expected = [847, 1047, 1177, 1107, 1007, 1017, 1147, 677, 1057, 1127, 1047, 1017, 1147, 1237, 837, 1177, 1127, 1017, 1147, 957, 837, 1057, 1097, 1127, 1087, 1017, 957, 777, 977, 1167, 1047, 957, 797, 1127, 1017, 1147, 977, 1167, 1057, 1117, 1107, 1257]

password = ''.join([chr((value - 7) // 10) for value in expected])
print("Password:", password)
```

Flag:
```
ThunderCipher{Super_Simple_Math_Operation}
```