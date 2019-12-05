import csv

score = []

with open('pliz.csv', newline='') as quiz:
  reader = csv.reader(quiz, delimiter=";")
  for row in reader:
    print(row[0])
    print(row[1], row[2], row[3])
    user = input("Выберите вариант ответа(а, б, в): ")

    if user == 'а':
      if row[1] == row[4]:
        print("Правильно!")
        score += 5
      else:
        print("Неправильно!")
    elif user == 'б':
      if row[2] == row[4]:
        print("Правильно!")
        score += 5
      else:
        print("Неправильно")
    elif user == 'в':
      if row[3] == row[4]:
        print("Правильно!")
        score += 5
      else:
        print("Неправильно!")
    else:
      print("Такого варианта ответа не существует!")

totalscore = sum(score)
print("Вы набрали " + str(totalscore) + " баллов)")


if totalscore == 100:
  print("Ваша оценка 'A'")
elif totalscore == 95:
  print("Ваша оценка '+B'")
elif totalscore == 90:
  print("Ваша оценка 'B'")
elif totalscore == 85:
  print("Ваша оценка '-B'")
elif totalscore == 80:
  print("Ваша оценка '+C'")
elif totalscore == 75:
  print("Ваша оценка 'C'")
elif totalscore == 70:
  print("Ваша оценка '-C'")
elif totalscore == 65:
  print("Ваша оценка 'D'")
elif totalscore == 60:
  print("Ваша оценка '-D'")
else:
  print("Ваша оценка 'F'")
