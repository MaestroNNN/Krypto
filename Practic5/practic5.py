
import hashlib
import os
import json

# Файл для хранения данных пользователей
USER_DATA_FILE = 'users.json'

def hash_password(password):
    """Хеширование пароля с использованием SHA-256."""
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, hashed_password

def save_user(username, password):
    """Сохранение пользователя в базу данных."""
    salt, hashed_password = hash_password(password)
    user_data = {
        'salt': salt.hex(),
        'hashed_password': hashed_password.hex()
    }
    
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            users = json.load(f)
    else:
        users = {}
    
    users[username] = user_data
    
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f)
    
    # Выводим соль и хешированный пароль в консоль
    print(f"Salt (hex): {salt.hex()}")
    print(f"Хешированный пароль (hex): {hashed_password.hex()}")

def verify_password(stored_password, salt, password):
    """Проверка пароля."""
    salt = bytes.fromhex(salt)
    stored_password = bytes.fromhex(stored_password)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hashed_password == stored_password

def authenticate(username, password):
    """Аутентификация пользователя."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            users = json.load(f)
        
        user_data = users.get(username)
        if user_data:
            salt = user_data['salt']
            stored_password = user_data['hashed_password']
            if verify_password(stored_password, salt, password):
                return True
    return False

if __name__ == "__main__":
    while True:
        choice = input("Выберите действие: [r]егистрация, [a]утентификация, [q]уит: ")
        if choice == 'r':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            save_user(username, password)
            print("Пользователь зарегистрирован!")
        elif choice == 'a':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            if authenticate(username, password):
                print("Аутентификация успешна!")
            else:
                print("Ошибка аутентификации.")
        elif choice == 'q':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
