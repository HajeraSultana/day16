print("Sing along: complete the song")
print()
print("Unleash your inner music buff: complete the song")
print()
count = 1
while True:
  color = input("I try to live in black and white, but I'm so ________  ")
  if color == "blue":
    break
  else:
    print("Not quite, give it another shot!")
    count += 1
    print()
print("Bravo! You finally got it right on your", count, "attempt!")