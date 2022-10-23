class Vigenere_cipher():
    def __init__(self, alphabet: str, string: str, key: str) -> None:
        """Ініціалізація переданих аргументів об'єкту класу."""
        self.alphabet = alphabet
        self.string = string
        self.key = key
    
    def generate_key(string: str, key: str) -> str:
        """Генерація ключа з ключового слова і переданого повідомлення."""
        key = list(key)

        if len(string) == len(key):
            return(key)
        else:
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
        
        return("".join(key))

    def encrypt(self) -> str:
        """Функція для шифрування методом Віженера."""
        self.encrypt_text = []

        for i in range(len(self.string)):
            x = (self.alphabet.find(self.string[i]) + self.alphabet.find(self.key[i])) % len(self.alphabet)
            x += self.alphabet.find('А')
            self.encrypt_text.append(self.alphabet[x])
        
        return("".join(self.encrypt_text))


    def decrypt(self) -> str:
        """Функція для дешифрування методом Віженера."""
        self.orig_text = []

        for i in range(len(self.encrypt_text)):
            x = (self.alphabet.find(self.encrypt_text[i]) - self.alphabet.find(self.key[i]) + len(self.alphabet)) % len(self.alphabet)
            x += self.alphabet.find('А')
            self.orig_text.append(self.alphabet[x])
        
        return("".join(self.orig_text))


def main():
    """Головна функція, що стартує після запуску файлу в інтерпретаторі."""
    alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ., "
    string = input().upper()
    keyword = "кейворд".upper()
    print(f"Алфавіт: {alphabet}\nВхідне повідомлення: {string}\nКлючове слово: {keyword}\n\n")

    key = Vigenere_cipher.generate_key(string, keyword)             # Створення ключа
    data = Vigenere_cipher(alphabet, string, key)                   # Створення об'єкту класу для шифрування методом Віженера

    print("Зашифроване повідомлення: ", data.encrypt())             # Виведення зашифрованого повідомлення
    print("Розшифроване повідомлення: ", data.decrypt())            # Виведення розшифрованого повідомлення


if __name__ == "__main__":
    main()