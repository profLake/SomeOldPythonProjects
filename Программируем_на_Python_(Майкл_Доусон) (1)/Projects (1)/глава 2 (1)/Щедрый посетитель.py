# Щедрый посетитель
# Считывает стоимость обеда и выводит
# расчётную сумму чаевых в 15 и 20% от него

print("Здравствуйте!")

coast = int(input("Введите сумму счёта за обед в "
                  "ресторане (в долларах): "))

print("Чаевые, составляющие 15% от стоимости обеда: ",
      str(coast / 100 * 15) + "$")
print("Чаевые, составляющие 20% от стоимости обеда: ",
      str(coast / 100 * 20) + "$")

input("До свидания!")
