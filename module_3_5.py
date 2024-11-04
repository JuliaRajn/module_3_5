def get_multiplied_digits(number):
  """Функция для подсчета произведения цифр числа."""

  str_number = str(number)
  first = int(str_number[0])
  if len(str_number) > 1:
    return first * get_multiplied_digits(int(str_number[1:]))
  else:
    return first

# Ввод числа пользователем
number = int(input("Введите целое число: "))

# Вызов функции и вывод результата
result = get_multiplied_digits(number)
print(result)
