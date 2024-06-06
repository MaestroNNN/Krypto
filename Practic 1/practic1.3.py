def caesar_decrypt(text, key):
    result = []
    for char in text:
        if char.isalpha():
            shift = ord(char) - key
            if char.islower():
                result.append(chr((shift - ord('a')) % 26 + ord('a')))
            elif char.isupper():
                result.append(chr((shift - ord('A')) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def decrypt(cipher_text):
    possible_texts = {}
    for key in range(26):
        possible_texts[key] = caesar_decrypt(cipher_text, key)
    return possible_texts

# Пример использования:

cipher_text = "Khoor"
possible_texts = decrypt(cipher_text)
print("Зашифрованный текст:", cipher_text)
for key, text in possible_texts.items():
    print(f"Ключ {key}: {text}")