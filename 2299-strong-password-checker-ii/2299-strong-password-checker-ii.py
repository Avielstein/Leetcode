class Solution(object):
    def strongPasswordCheckerII(self, password):
        '''
        1.It has at least 8 characters.
        2. It contains at least one lowercase letter.
        3. It contains at least one uppercase letter.
        4. It contains at least one digit.
        5. It contains at least one special character. 
            The special characters are the characters in the following string: "!@#$%^&*()-+".
        6. It does not contain 2 of the same character in adjacent positions 
            (i.e., "aab" violates this condition, but "aba" does not).
        '''
        
        upper   = False #2
        lower   = False #3
        num     = False #4
        special = False #5
        
        
        # check 1
        if len(password)<8:
            return False
        
        for i in range(len(password)):
            item = password[i]
            if item.isupper():
                upper=True
            if item.islower():
                lower=True
            if item.isnumeric():
                num=True
            if item in "!@#$%^&*()-+":
                special=True
            #check for repeat
            
            if i>0 and item==password[i-1]:
                return False
        
        if upper and lower and num and special:
            return True
        else:
            return False
        
        
            
                
            
