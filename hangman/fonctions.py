#!/usr/bin/python3.8

# -*-coding:UTF-8 -*
import data


import random


def generation_word():
	word = random.choice(data.word_dictionnary)
	return word

def word_validation(word):
	data.word_to_find = word
	data.word_to_print = len(word)*"*"


def letter_check(letter):
	if letter in data.word_to_find:
		return letter, True, find_place_letter(letter)
	else:
		return letter, False

def find_place_letter(letter):
	places = []
	for index,l in enumerate(data.word_to_find):
		if letter == l:
			places.append(index)
	return places

def ask_letter():
	can_play = False
	while not can_play:
		letter = input("Please choose a letter: ")
		can_play, message = can_play_letter(letter)
		print(message)
	save_letter(letter)

def can_play_letter(letter):
	if not letter.isalpha():
		message = "This is not a playable character"
		return False, message
	elif letter in data.false_letters or letter in data.found_letters:
		message = "You've already played this letter"
		return False, message
	else:
		message = "Let's go"
		return True, message

def update_word_to_print(list_letter):
	word_buffer =list(data.word_to_print)
	for index in list_letter:
		word_buffer[index]=data.word_to_find[index]
	data.word_to_print="".join(word_buffer)

def check_word_find():
	if data.word_to_print == data.word_to_find:
		return True

def send_letter_good_false(letter_boolean):
	if letter_boolean[1]:
		data.found_letters.append(letter_boolean[0])
		update_word_to_print(letter_boolean[2])
		print("Good guess")
	else:
		data.false_letters.append(letter_boolean[0])
		lose_life()
		print('Bad guess')

def save_letter(letter):
	send_letter_good_false(letter_check(letter))

def end_game():
	if data.lives==0:
		return True
	elif check_word_find== True:
		return True
	else:
		return False

def after_end_game():
	if data.lives==0:
		return "You lost all your lives"
	elif check_word_find== True:
		return "You found the word!"
# Validated

#def nom_joueur():
	# demande le nom du joueur 
	# enregistre ce nom dans donnes

#def enregistrer_score():
	# ouvre ou crée fichier scores
	# enregistre son nom avec le score 0

def lose_life():
	data.lives -= 1
	return data.lives
	print(send_letter_good_false)

def tour():
	print(data.word_to_print)
	ask_letter()
	print("Bad letters : ",data.false_letters)
	print("Letters found : ",data.found_letters)
	print("Lives : ", data.lives)

