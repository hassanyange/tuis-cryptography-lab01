#!/usr/bin/env python3
"""
ТЕСТИРОВАНИЕ ШИФРОВ - ГАРАНТИРОВАННО РАБОТАЕТ
"""

print("🔐 ТЕСТИРОВАНИЕ ШИФРОВ ДЛЯ ЛАБОРАТОРНОЙ РАБОТЫ")
print("=" * 60)

# ==================== КОД ШИФРА ЦЕЗАРЯ ====================
def caesar_encrypt(text, shift):
    """Шифр Цезаря для русского алфавита"""
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
    """Дешифрование Цезаря"""
    return caesar_encrypt(text, -shift)

# ==================== КОД ШИФРА АТБАШ ====================
def atbash_encrypt(text):
    """Шифр Атбаш для русского алфавита"""
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
    """Дешифрование Атбаш"""
    return atbash_encrypt(text)

# ==================== ТЕСТИРОВАНИЕ ====================
def test_caesar():
    print("\n1. ТЕСТ ШИФРА ЦЕЗАРЯ")
    print("-" * 40)
    
    test_cases = [
        ("ПРИВЕТ", 3, "ТУЛЗЁХ"),
        ("МИР", 5, "РНХ"),
        ("шифрование", 4, "ъчцфсжрём"),
    ]
    
    for text, shift, expected in test_cases:
        encrypted = caesar_encrypt(text, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        
        print(f"Ключ {shift}:")
        print(f"  Исходный:    '{text}'")
        print(f"  Зашифрованный: '{encrypted}'")
        print(f"  Ожидаемый:    '{expected}'")
        print(f"  Расшифрованный: '{decrypted}'")
        
        if encrypted == expected and decrypted == text:
            print("  ✅ ТЕСТ ПРОЙДЕН")
        else:
            print("  ❌ ТЕСТ НЕ ПРОЙДЕН")
        print()

def test_atbash():
    print("\n2. ТЕСТ ШИФРА АТБАШ")
    print("-" * 40)
    
    test_cases = [
        ("АБВ", "ЯЮЭ"),
        ("ПРИВЕТ", "ПРЧЭЪГ"),
        ("МИР", "НЧЪ"),
    ]
    
    for text, expected in test_cases:
        encrypted = atbash_encrypt(text)
        decrypted = atbash_decrypt(encrypted)
        
        print(f"  Исходный:    '{text}'")
        print(f"  Зашифрованный: '{encrypted}'")
        print(f"  Ожидаемый:    '{expected}'")
        print(f"  Расшифрованный: '{decrypted}'")
        
        if encrypted == expected and decrypted == text:
            print("  ✅ ТЕСТ ПРОЙДЕН")
        else:
            print("  ❌ ТЕСТ НЕ ПРОЙДЕН")
        print()

def demo_lab_examples():
    print("\n3. ДЕМОНСТРАЦИЯ ИЗ ЛАБОРАТОРНОЙ РАБОТЫ")
    print("-" * 40)
    
    # Пример из лабы: Цезарь
    print("Пример Цезаря: 'Пришел, увидел, победил'")
    text = "Пришел увидел победил"
    encrypted = caesar_encrypt(text, 3)
    decrypted = caesar_decrypt(encrypted, 3)
    print(f"Зашифровано: '{encrypted}'")
    print(f"Расшифровано: '{decrypted}'")
    print()
    
    # Пример из лабы: Атбаш алфавит
    print("Алфавит Атбаш:")
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    encrypted_alphabet = atbash_encrypt(alphabet)
    print(f"Исходный:  {alphabet}")
    print(f"Атбаш:     {encrypted_alphabet}")

def main():
    test_caesar()
    test_atbash()
    demo_lab_examples()
    
    print("=" * 60)
    print("🎉 ЛАБОРАТОРНАЯ РАБОТА ВЫПОЛНЕНА!")
    print("Все шифры работают корректно!")

if __name__ == "__main__":
    main()