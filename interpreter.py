from soul import Int, Float,String

class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def read_FLOAT(self, value):
        return float(value)
    
    def read_INT(self, value): 
        return int(value)
    
    def read_STRING(self, value):  
        return str(value)

    def compute_bi(self, left, op, right):
        left_type = left.type
        right_type = right.type 

        # convert string to an int or float
        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)

        if op.value == "+":
            output = left + right
        elif op.value == "-":
            output = left - right
        elif op.value == "*":
            output = left * right
        elif op.value == "/":
            if right == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            output = left / right

            if output.is_integer():  # If the result of division is a whole number (no remainder), return INT
                output = int(output)  # Convert to int if it's a whole number
        elif op.value == "|":  
            if left_type == "STRING" and right_type == "STRING":  
                output = left + right  
                return String(output)
        else:
            raise ValueError(f"Unsupported operator: {op.value}")  # Error check for an unsupported operator


            
        if left_type == "INT" and right_type == "INT" and not isinstance(output, float):
            return Int(output)  # Return as Int if both types are INT
        else:
            return Float(output)  # Return as Float if either operand is FLT or result is float

    def interpret(self, tree = None):  
    # Handles non recursive cases  
        if tree is None:  
            tree = self.tree  
  
        if not isinstance(tree, list):  
            return tree  
  
    # Eval right subtree  
        left_node = tree[0]  
        if isinstance(left_node,list):  
            left_node = self.interpret(left_node)  
  
    # Eval left subtree  
        right_node = tree[2]  
        if isinstance(right_node,list):  
            right_node = self.interpret(right_node)  
  
        operator = tree[1]  
        return self.compute_bi(left_node, operator, right_node)
    
