print("Welcome to Guess the Number")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")
print()

number = 1000
count = 1

while True:
  guess = int(input("Guess a number: "))
  if guess < 0:
    print("Negative numbers are not allowed. Now we'll never know the number.")
    exit()
  elif guess < number:
    print("Your guess is too low. Try again!")
    print()
  elif guess > number:
    print("Your guess is too high. Try again!")
    print()
  elif guess == number:
    break
  else:
    print("Hmm, I don't recognize that number.")
  count += 1
print()
print(f"You guessed the secret number: {number}, in {count} tries! ")