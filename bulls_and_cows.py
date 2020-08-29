class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_array = [x for x in secret]
        guess_array = [y for y in guess]
        
        # Match the bulls
        bulls = 0
        index = 0
        while(index < len(secret_array)):
            if(secret_array[index] == guess_array[index]):
                bulls += 1
                secret_array.pop(index)
                guess_array.pop(index)
            else:
                index += 1
        
        # Match the cows
        cows = 0
        index = 0
        while(index < len(secret_array)):
            if(secret_array[index] in guess_array):
                cows += 1
                guess_index = guess_array.index(secret_array[index])
                guess_array.pop(guess_index)
                secret_array.pop(index)
            else:
                index += 1
                
        return(str(bulls) + "A" + str(cows) + "B")
    
# Thought the guess might have more or less digits than the secret number
# Scenarios:
# s = 1807 g = 7810
# s = 1123 g = 0111
# s = 1113 g = 0101

# scenario which s = 1113 and guess = 0101
# after matching bulls s = 113 and guess = 001
