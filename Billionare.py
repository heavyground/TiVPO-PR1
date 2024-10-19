import random

questions = [
    {
        "text": "Какой язык программирования используется для разработки ис-кусственного интеллекта?",
        "answers": ["Java", "C++", "Python", "Ruby"],
        "correct": 3
    },
    {
        "text": "Как называется столица Франции?",
        "answers": ["Берлин", "Мадрид", "Париж", "Лондон"],
        "correct": 3
    },
        {
        "text": "Какое число является квадратным корнем из 64?",
        "answers": ["6", "7", "8", "9"],
        "correct": 3
    },
    {
        "text": "Кто написал роман 'Преступление и наказание'?",
        "answers": ["Лев Толстой", "Фёдор Достоевский", "Антон Чехов", "Александр Пушкин"],
        "correct": 2
    },
    {
        "text": "В каком году произошла Октябрьская революция?",
        "answers": ["1914", "1917", "1922", "1936"],
        "correct": 2
    },
    {
        "text": "Как называется крупнейшая планета Солнечной системы?",
        "answers": ["Земля", "Марс", "Юпитер", "Сатурн"],
        "correct": 3
    },
    {
        "text": "Как называется химический элемент с атомным номером 1?",
        "answers": ["Кислород", "Гелий", "Водород", "Углерод"],
        "correct": 3
    },
    {
        "text": "Какой ученый разработал теорию относительности?",
        "answers": ["Ньютон", "Эйнштейн", "Максвелл", "Тесла"],
        "correct": 2
    },
    {
        "text": "В каком году распался Советский Союз?",
        "answers": ["1989", "1991", "1993", "1995"],
        "correct": 2
    },
    {
        "text": "Кто является автором картины 'Звездная ночь'?",
        "answers": ["Клод Моне", "Пабло Пикассо", "Винсент ван Гог", "Саль-вадор Дали"],
        "correct": 3
    },
    {
        "text": "Как называется элемент таблицы Менделеева с символом 'Fe'?",
        "answers": ["Фосфор", "Железо", "Фтор", "Франций"],
        "correct": 2
    },
    {
        "text": "Как называется первый искусственный спутник Земли, запущен-ный в 1957 году?",
        "answers": ["Аполлон-11", "Спутник-1", "Восток-1", "Союз-1"],
        "correct": 2
    }
    
]

# Функция для проверки ответа
def check_answer(question, answer):
    return question['correct'] == answer

# Функция старта игры
def start_game():
    return {
        "current_question": 1,
        "balance": 0
    }

# Функция для выбора игрока
def player_choice(choice, game_state):
    if choice == "exit":
        return "exit"
    else:
        return "continue"

# Функция для отображения вопроса
def display_question(question):
    print(f"Вопрос: {question['text']}")
    for i, answer in enumerate(question['answers'], 1):
        print(f"{i}. {answer}")

def ask_question(question):
    display_question(question)
    user_answer = int(input("Ваш ответ (1-4): "))
    return check_answer(question, user_answer)

def millionaire_game():
    game_state = start_game()
    total_questions = len(questions)
    winnings = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

    for i in range(total_questions):
        current_question = questions[game_state['current_question'] - 1]
        print(f"\nВопрос {game_state['current_question']}: Сумма за вопрос: {winnings[game_state['current_question'] - 1]}")

        if ask_question(current_question):
            game_state["balance"] = winnings[game_state['current_question'] - 1]
            print(f"Правильно! Ваш баланс: {game_state['balance']}")

            choice = input("Хотите продолжить (y/n)? ")
            if choice.lower() == 'n':
                print(f"Вы уходите с суммой {game_state['balance']}. Игра завершена.")
                break
        else:
            print("Неправильно! Вы проиграли. Игра завершена.")
            break

        game_state["current_question"] += 1

    if game_state["current_question"] == total_questions + 1:
        print(f"Поздравляем! Вы выиграли {game_state['balance']}!")

if __name__ == "__main__":
    start = input("Начать игру? (y/n): ")
    if start.lower() == 'y':
        millionaire_game()
    else:
        print("Игра завершена.")
