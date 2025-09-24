# Constants

DIGITS = "0123456789"
OP = "+-/*|"

# Lexer

class Lexer:
    
    def __init__(self,text):
        self.text = text
        self.index = 0
        self.tokens = []
        self.current_char = self.text[self.index]
        self.token = None

    def tokenize(self):
        while self.index < len(self.text):
            if self.current_char in ' \t':  
                self.advance()

            elif self.current_char in DIGITS:  
                self.tokens.append(self.create_number())

            elif self.current_char == '"':
                self.tokens.append(self.create_word())

            elif self.current_char in OP:   
                self.tokens.append(Operation(self.current_char))
                self.advance()

            else:
                raise ValueError(f"Invalid character {self.current_char}")

        return self.tokens

    def create_number(self):
        number = ""
        dot_count = 0
        while (self.current_char in DIGITS or self.current_char == ".") and (self.index < len(self.text)):
            
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                number += '.'
            else:
                number += self.current_char
            
            self.advance()

        if dot_count == 0:
            return Int(number)
        else: 
            return Float(number)
        
    def create_word(self):
        word = ""
        self.advance()  
        while self.current_char != '"' and self.index < len(self.text):            
            word += self.current_char
            self.advance()
        self.advance()
        
        return String(word)
        
    
    def advance(self):
        self.index += 1
        if self.index < len(self.text):
            self.current_char = self.text[self.index]

#Tokenization 

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def  __repr__(self):
        return str(self.value)
    
class Int(Token):
    def __init__(self, value):
        super().__init__("INT", value)

class Float(Token):
    
    def __init__(self,value):
        super().__init__("FLOAT",value)

class Operation(Token):
    def __init__(self,value):
        super().__init__("OP",value)

class String(Token):
    def __init__(self,value):
        super().__init__("STRING",value)



