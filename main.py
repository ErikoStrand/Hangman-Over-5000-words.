import numpy as np
import os
import hangman as f
import ast
import time
used = []
liv = 7
word_show = []
gubbe = 0
vit = 0
last = []

# start up stuff
with open('data.txt') as t:
    data = t.read()
data = ast.literal_eval(data)  
os.system("clear")
my_file = open("words.txt")
words = my_file.readlines()
words = [x[:-1] for x in words]


# saves data
def save():
  with open('data.txt', 'w') as f:
    f.write(str(data))
  
def animation(i):
  for x in range(i):
    os.system("clear")
    # print(*word)
    try:
      print(data["win"], "🏆", " {0:.0%}".format(data["win"]/data["total"]))
      print(data["lost"], "❌", "{0:.0%}".format(data["lost"]/data["total"]))
    except:
      pass
    print("Last Word:", *last)
    print(f.man[gubbe+x])
    print("Used:", *used)
    print(f"Clue:", *word_full)
    print(liv*"❤️ " + vit*"🤍")
    print(*word_show)
    if liv <= 0:
      print("❌❌❌ \nthe word was", *word)
      time.sleep(0.25)
   
# resets the data for the next word    
def reset():
  global used, liv, word_show, gubbe, vit, last
  last = []
  last.append("".join(word))
  used = []
  liv = 7
  word_show = []
  gubbe = 0
  vit = 0
  save()
  rand_word()
   

# chooses a random word for the user to guess
def rand_word():
  global words, word, word_show, word_full, last
  word_full = np.random.choice(words)
  word_full = word_full.split()
  word = word_full[0].upper()
  word_full.pop(0)
  word = (" ".join(word))
  word = word.split()
  for x in range(len(word)):
    word_show.append("_")

# takes user input to check if they are in the random word
def gissa():
  global guess, word_show, liv, used, gubbe, vit, word
  os.system("clear")
  animation(1)
  guess = input("Word > ").upper()
  guess = (" ".join(guess))
  guess = guess.split()
  for x in range(len(guess)):
    if guess[x] not in used:
      used.append(guess[x])
      if guess[x] not in word:
        liv -= 1
        vit += 1
        gubbe += 1
      if liv <= 0:
        break
      
    if guess[x] in word:
      for y in range(len(word)):
        if guess[x] in word[y]:
          word_show.pop(y)
          word_show.insert(y, word[y])
rand_word()

# the main loop to check if you win or lose, and give the stats according to it.
while True:
  gissa()
  animation(1)
  if liv <= 0:
    animation(6)
    data["lost"] += 1
    data["total"] += 1
    reset()
    
  if word_show == word:
    animation(0)
    print("You won!", "🏆")
    time.sleep(2)
    data["win"] += 1
    data["total"] += 1
    reset()