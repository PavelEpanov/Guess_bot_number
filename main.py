import random


def main():
	num = get_bot_number()
	degree = get_degree()
	user_answer(num, degree)


def get_bot_number():
	return random.randint(1, 10)


def get_degree():
	return random.randint(2, 5)


def user_answer(bot_number, degree):
	print(f"'X' - {bot_number ** degree} в степени {degree}")
	answer = int(input("X: "))
	if answer == bot_number:
		print("Красава, мужик!!!!111111 Твой ответ верен")
	else:
		while answer != bot_number:
			print("Неправильно! Введи ответ снова")
			answer = int(input("X =  "))
		if answer == bot_number:
			print("Красава, мужик!!!!111111 Твой ответ верен")

main()

