import socket
import re
from collections import Counter

HOST = "216.107.139.152"
PORT = 8989

def is_vowel(char):
    return char.lower() in 'aeiou'

def is_special_character(char):
    return char in '@#_&-+]|$!'

def next_alphabet_char(char):
    return chr(((ord(char.lower()) - 97 + 1) % 26) + 97)

def calculate_s(word, n):
    size = len(word)
    somme = 0
    for i in range(n, size):
        z = ord(next_alphabet_char(word[i]))
        V = 1 if is_vowel(word[(i + 1) % size]) else 0
        G = i if is_special_character(word[(i - 1) % size]) else 23
        somme += i * z ** V + (G % 7)
    return somme

def is_vowel(char):
    return char.lower() in 'aeiou'

def is_special_char(char):
    return char in '@#_&-+]|$!'

def next_alphabetical_char(char):
    if char.isalpha():
        if char == 'z':
            return 'a'
        elif char == 'Z':
            return 'A'
        else:
            return chr(ord(char) + 1)
    return char

def apply_rule_6(word):
    size = len(word)
    result = []

    for n in range(size):
        current_char = word[n]
        if current_char.lower() not in 'aeiou':  # Check if consonant
            s = 0
            for i in range(n, size):
                z = ord(next_alphabetical_char(word[i]))
                V = 1 if is_vowel(word[(n + 1) % size]) else 0
                G = n if n > 0 and is_special_char(word[n - 1]) else 23
                s += i * z ** V + (G % 7)

            c = ord(current_char)
            new_char = chr((c + s) % 95 + 32)
            result.append(new_char)
        else:
            result.append(current_char)

    return ''.join(result)

def apply_rule_5(word, shift):
    if len(word) % 2 == 1:
        # Shift letters to the right by the extracted shift value
        og_word = word
        shift = shift % len(word)
        word = word[-shift:] + word[:-shift]
        
        # Replace the last letter with the most frequently used vowel
        vowels = [char for char in og_word if is_vowel(char)]
        if vowels:
            freq_vowels = Counter(vowels)
            sorted_vowels = sorted(freq_vowels.items(), key=lambda x: (-x[1], og_word.index(x[0])))
            most_common_vowel = sorted_vowels[0][0]
            
            word = word[:-1] + most_common_vowel
    else:
        # Replace 't' with 'p' and 'c' with 'z'
        word = word.replace('t', 'p').replace('T', 'P').replace('c', 'z').replace('C', 'Z')
    
    return word


def receive_until(sock, pattern):
    data = b""
    while not re.search(pattern, data.decode(), re.DOTALL):
        chunk = sock.recv(4096)
        if not chunk:
            break
        data += chunk
    return data.decode()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        data = receive_until(s, r"\}")
        print(data)
        word = re.search(r"\{(.+?)\}", data).group(1)
        s.sendall((word + "\n").encode())
        print("Sent: " + word)
        
        for i in range(101):
            data = receive_until(s, r"\}")
            print(data)
            rule_number = re.search(r"Rule (\d+)", data).group(1)
            word = re.search(r"\{(.+?)\}", data).group(1)
            if rule_number == "6":
                word = apply_rule_6(word)
                s.sendall((word + "\n").encode())
                print("Sent: " + word)
            elif rule_number == "2":
                word = word[::-1]
                s.sendall((word + "\n").encode())
                print("Sent: " + word)
            elif rule_number == "3":
                vowels = 'aeiou'
                vowels_map = {'a':'e', 'e':'i', 'i':'o', 'o':'u', 'u':'a'}
                new_word = ''
                for char in word:
                    if char.lower() in vowels:
                        new_word += vowels_map[char.lower()] if char.islower() else vowels_map[char.lower()].upper()
                    else:
                        new_word += char
                
                new_new_word = new_word[-1] + new_word[1:-1] + new_word[0]
                s.sendall((new_new_word + "\n").encode())
                print("Sent: " + new_new_word)
            elif rule_number == "4":
                word = word.replace('e', '3').replace('i', '1').replace('o', '0').replace('s', '5').replace('a','@')
                s.sendall((word + "\n").encode())
                print("Sent: " + word)
            elif rule_number == "5":
                shift_match = re.search(r"Shift the letters to the right by (\d+)", data)
                if shift_match:
                    shift_value = int(shift_match.group(1))
                    word = apply_rule_5(word, shift_value)
                    s.sendall((word + "\n").encode())
                    print("Sent: " + word)
            else:
                s.sendall((word + "\n").encode())
                print("Sent: " + word)

if __name__ == "__main__":
    main()