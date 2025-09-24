def atbash_encrypt(text):
    """
    Шифр Атбаш для русского алфавита
    """
    result = ""
    for char in text:
        if 'а' <= char <= 'я':
            result += chr(ord('я') - (ord(char) - ord('а')))
        elif 'А' <= char <= 'Я':
            result += chr(ord('Я') - (ord(char) - ord('А')))
        else:
            result += char
    return result

def atbash_decrypt(text):
    """
    Дешифрование Атбаш
    """
    return atbash_encrypt(text)

if __name__ == "__main__":
    # Simple test when run directly
    text = "АБВ ЯЮЭ"
    encrypted = atbash_encrypt(text)
    decrypted = atbash_decrypt(encrypted)
    print(f"Исходный: {text}")
    print(f"Зашифрованный: {encrypted}")
    print(f"Расшифрованный: {decrypted}")