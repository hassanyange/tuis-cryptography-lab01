def caesar_encrypt(text, shift):
    """
    Шифр Цезаря для русского алфавита
    """
    result = ""
    for char in text:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            if char.isupper():
                base = ord('А')
                alphabet_size = 32
            else:
                base = ord('а')
                alphabet_size = 32
            shifted = (ord(char) - base + shift) % alphabet_size
            result += chr(shifted + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    """
    Дешифрование Цезаря
    """
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    # Simple test when run directly
    text = "ПРИВЕТ МИР"
    shift = 3
    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Исходный: {text}")
    print(f"Зашифрованный: {encrypted}")
    print(f"Расшифрованный: {decrypted}")