import random
match=0
print("\n")
print("Decide which player will be player1 and who will be player2 and go accordingly\n")
for i in range(5):
  turn=random.randint(1,2)
  a=int(input(f"player {turn} chose a number from 0 to 9: "))
  b=int(input(f"player {3-turn} chose a number from 0 to 9: "))
  match+=a+b+random.randint(0,9)
  a_guess=int(input(f"player {turn} Guess the number: "))
  b_guess=int(input(f"player {3-turn} guess the number: "))
  if(match==a_guess):
    print(f"Game over player {turn} won")
    break
  elif(match==b_guess):
    print(f"Game over player {3-turn} won")
    break
  else:
    print("Next round")
  if(i==4):
    winner=turn if abs(match-a_guess)<abs(match-b_guess) else 3-turn
    print(f"Oops it seems none of you guessed it right \nwinning score = {match}\nClosed was player {winner}")
