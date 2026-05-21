import base64


def vigenere_cipher(text, key, mode="encrypt"):
    result = ""
    key = key.upper()
    key_idx = 0

    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            k_val = ord(key[key_idx % len(key)]) - ord("A")

            if mode == "encrypt":
                new_char = chr((ord(char) - start + k_val) % 26 + start)
            else:
                new_char = chr((ord(char) - start - k_val) % 26 + start)

            result += new_char
            key_idx += 1
        else:
            result += char

    return result


def xor_encrypt(text, key):
    encrypted = bytes([
        ord(c) ^ ord(key[i % len(key)])
        for i, c in enumerate(text)
    ])

    return base64.b64encode(encrypted).decode()


def xor_decrypt(encoded_text, key):
    encrypted = base64.b64decode(encoded_text)

    decrypted = "".join([
        chr(byte ^ ord(key[i % len(key)]))
        for i, byte in enumerate(encrypted)
    ])

    return decrypted