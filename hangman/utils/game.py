
import random

class Hangman():
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    
    #Play method
    def __init__(self):
        self.word_to_find = list(random.choice(Hangman.possible_words))
        
        self.lives = 5
        self.turn_count = 0
        self.error_count = 0
    
        self.wrongly_guessed_letters = []
        self.correctly_guessed_letters = len(self.word_to_find) * ['_']
    
    def play(self):
        letter_guess = input("Enter your letter : ")
            
        if len(letter_guess) != 1:
            print("Please enter a single letter")
        elif not letter_guess.isalpha():
            print('Please enter a LETTER.') 
        else:
            print("You're guess is " + letter_guess)
            
        if letter_guess in self.word_to_find:
            for index, character in enumerate(self.word_to_find):
                if letter_guess == character:
                    self.correctly_guessed_letters[index] = letter_guess
        else:
            print("Sorry, wrong guess")
            self.wrongly_guessed_letters.append(letter_guess)
            self.error_count += 1
            self.lives -= 1
            
        self.turn_count += 1
            
        
    #Start_game method 
    def start_game(self):
        ''' Starts the game .....'''            

        while True:
            if self.word_to_find == self.correctly_guessed_letters:
                self.well_played() 
                break
            
            if self.lives == 0:
                self.game_over()
                break
            
            self.play()
            print(self.correctly_guessed_letters)
            
    #Well played method 
    def well_played(self):
        '''A method that will print a win message, showing the secret word (word_to_find),
        how many turns it took to discover and the number of error from the player.'''
        
        print(f"Congrats!! You found the word: {self.word_to_find} in {self.turn_count} turns and {self.error_count} errors!")
     
    #Game over method    
    def game_over(self):
        '''Call the game over when there is no more lives'''
        print("Game Over! Best luck next time!")
        
if __name__ == "__main__":
    hangman = Hangman()
    hangman.start_game()
