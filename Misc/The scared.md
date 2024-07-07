**Description**: I heard Thunder Cipher has some really cool posts on their socials. I loved their story about the villa!

Also someone from their page sent me this: $2b$12$p5jVqnJoUZk2CCRJGbqjUODe4d/BZ3CCEyeP1kAc9tk4iqwmJrovC

Guidance - When the time for the cracking comes, you'll need this: NjYgNjkgNmUgNjQgNjkgNmUgNjcgMjAgNjYgNmYgNzIgNmQgNjEgNzQgM2EgMjAgNzcgNmYgNzIgNjQgMzEgNzcgNmYgNzIgNjQgMzIgNzcgNmYgNzIgNjQgMzM=

<hr>

Decoded The Cipher using `CyberChef`.

<figure><img src="../src/Misc/The scared/dec.png"></figure>

I went to the instagram post which had the following description.

```
000mgggg, you won't believe what happened at the bcrypt villa today! It all started with a quiet morning, but then everything changed. Suddenly, this b1g and 5c4ry rat appeared out of nowhere, creeping around the house and causing quite a stir. Everyone in the villa was s4d and freaked out, especially after hearing strange noises coming from the kitchen. My friend h3pp3, who usually isn't fazed by much, was absolutely terrified. We all tried to keep calm and figure out a plan. Meanwhile, my d0g, who is usually a brave soul, was barking non-stop, while the c4t was nowhere to be found, probably hiding in some secret spot. It was a scene straight out of a horror movie! We need help to get this unwelcome guest out of here ASAP. If anyone has any tips or tricks for dealing with a massive rat invasion, please let us know. The Thing lurking in our house has got everyone on edge! (Hint: Pay attention to the characters that stand out in the words here, they might just be the words to decode!).
```

So the words that stood out were `000mgggg`, `b1g`, `5c4ry`, `s4d`, `h3pp3`, `d0g`, `c4t`.

I generated a wordlist of 3 words according to the hint.


```py
import itertools

words = ["000mgggg", "b1g", "5c4ry", "s4d", "h3pp3", "d0g", "c4t"]

# Generate all combinations of 3 words
combinations_of_3 = list(itertools.combinations(words, 3))

# Generate permutations for each combination
with open("wordlist.txt", "w") as f:
    for combination in combinations_of_3:
        permutations = list(itertools.permutations(combination))
        for permutation in permutations:
            # Join words without spaces
            password = ''.join(permutation)
            f.write(password + "\n")

print("Wordlist has been generated and saved to wordlist.txt")
```
Bruteforced the hash using the generated wordlist.

<figure><img src="../src/Misc/The scared/brute.png"></figure>

Flag:
```
ThunderCipher{b1g5c4ryc4t}
```