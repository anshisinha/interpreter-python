from tokens import TokenType, Token

WHITESPACE = ' \n\t'
DIGITS = '0123456789'


class Lexer:

    #This constructor takes in the text that is to be processed
    def __init__(self, text):
        self.text = iter(text)
        self.advance() #advances to the first character

    #This method will move onto the next character and
    #store it in self.current_char
    def advance(self):
        #because we have defined self.text as an iterator,
        #we can use the next() function to give us the next char
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    #This function will generate all the tokens from the input text
    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"ILLEGAL CHARACTER '{self.current_char}'")

    #Goes through the string and generates numbers
    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str

        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))

