import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, що знаходить усі дійсні числа в тексті та повертає їх по черзі.

    Параметри:
    text (str): Вхідний рядок, що містить текст із числами.

    Повертає:
    Generator[float, None, None]: Генератор, що повертає числа у вигляді float.
    """
    
    pattern = r'\b\d+(?:\.\d+)?\b'
    
    
    matches = re.findall(pattern, text)
    
    
    for match in matches:
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює суму всіх чисел, що знайдені генератором у тексті.

    Параметри:
    text (str): Вхідний рядок, що містить текст із числами.
    func (Callable): Функція, що повертає генератор чисел з тексту.

    Повертає:
    float: Загальна сума чисел у тексті.
    """
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)


print(f"Загальний дохід: {total_income:.2f}")