def upper_case_string(input_string):
    """
    Принимает строку и возвращает ее в верхнем регистре
    """
    return input_string.upper()


def capitalize_words(input_string):
    """
    принимает строку и возвращает с заглавной буквы каждое слово этой строки
    """
    return ' '.join(word.capitalize() for word in input_string.split())
