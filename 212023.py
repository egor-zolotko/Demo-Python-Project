import re

def is_strong_password(password):
    # Проверка длины пароля
    if len(password) < 8:
        return False

    # Проверка наличия хотя бы одной заглавной буквы
    if not re.search(r"[A-Z]", password):
        return False

    # Проверка наличия хотя бы одной строчной буквы
    if not re.search(r"[a-z]", password):
        return False

    # Проверка наличия хотя бы одной цифры
    if not re.search(r"\d", password):
        return False

    # Проверка наличия хотя бы одного специального символа
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True

def password_strength(password):
    score = 0

    # Добавление баллов за длину пароля
    score += len(password) // 2

    # Добавление баллов за наличие разных типов символов
    types_of_characters = 0
    if re.search(r"[a-z]", password):
        types_of_characters += 1
    if re.search(r"[A-Z]", password):
        types_of_characters += 1
    if re.search(r"\d", password):
        types_of_characters += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        types_of_characters += 1

    score += (types_of_characters - 1) * 10

    return score

def main():
    password = input("Введите пароль для анализа: ")

    if is_strong_password(password):
        print("Пароль считается сильным.")
    else:
        print("Пароль не соответствует требованиям безопасности.")

    score = password_strength(password)
    print("Оценка стойкости пароля:", score)

    if score < 50:
        decision = input("Оценка стойкости пароля низкая. Желаете изменить пароль? (yes/no): ").lower()
        if decision == "yes":
            new_password = input("Введите новый пароль: ")
            print("Пароль успешно изменен.")
        else:
            print("Пароль остается без изменений.")
    else:
        print("Пароль оценен как стойкий. Нет необходимости в изменении.")

if __name__ == "__main__":
    main()
