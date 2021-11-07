
replay = True 
while replay:


    number_to_guess = 77

    score = 0
    game_over = False
    while not game_over:
        guess = int(input('Please enter a number between 1 and 100'))
        
        if guess < number_to_guess:
            print('Your guess is too low')
            score += 1
            
        elif guess > number_to_guess:
            print('Your guess is too high')
            score -= 1
        else:
            print('You are correct!')
            print('Your score was' + str(score))
            game_over = True 
    again = input('Would you like to play again (y/n)')
    if again == "n":
        replay = False
        