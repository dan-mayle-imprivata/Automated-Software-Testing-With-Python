movies_watched = {"The Matrix", "Blade", "Deadpool"}
user_movie = input("Enter something you have watched recently: ").lower()

if user_movie in movies_watched:
    print(f"I have watched {user_movie} too!")
else:
    print("I have not seen that movie yet.")


number = 7
user_input = input("Enter 'y' if you would like to play")

if user_input == 'y':
    user_number = int(input("Guess out number"))
    if user_number == number:
        print("You guessed right!")
    elif abs(number - user_number) == 1:  # abs changes negative number to positive
        print("You were off by one/")
    else:
        print("Sorry, it is wrong!")
