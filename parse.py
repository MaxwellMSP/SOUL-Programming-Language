class Parser:
    def __init__(self, tokens):
        self.tokens = tokens    
        self.index = 0
        self.token = self.tokens[self.index]

    def factor(self):  
        if self.token.type == "INT" or self.token.type == "FLOAT":  
            token = self.token  
            self.advance()  
            return token  
        elif self.token.type == "STRING":  
            token = self.token  
            self.advance()  
            return token
        
    def term(self):
        left_node = self.factor()

        while self.token.value == "*" or self.token.value == "/":
            operation = self.token
            self.advance()
            right_node = self.factor()
            left_node = [left_node, operation, right_node]

        return left_node

    def expression(self):
        left_node = self.term()

        while self.token.value in ["+", "-", "|"]:            
            operation = self.token
            self.advance()
            right_node = self.term()
            left_node = [left_node, operation, right_node]

        return left_node

    def parse(self):  
        if len(self.tokens) == 1:  
            return self.tokens[0]  
        return self.expression() 
    
    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.token = self.tokens[self.index]