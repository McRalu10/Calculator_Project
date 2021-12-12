from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'
USEFUL_LETTERS = 'LOGRADCSINTlogradcsint'  # used letters in LOG, RAD, COS, SIN, TAN


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
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
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '^':
                yield self.check_power()
            elif self.current_char in USEFUL_LETTERS:
                yield self.check_available_tokens()
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char == '.' or self.current_char in DIGITS):
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

    def check_power(self):
        current_token = self.current_char
        self.advance()
        current_token += self.current_char

        if current_token == '^^':
            self.advance()
            return Token(TokenType.POWER)
        else:
            raise Exception(f"Illegal character '{current_token}'")

    def check_available_tokens(self):
        current_token = self.current_char
        self.advance()
        current_token += self.current_char
        self.advance()
        current_token += self.current_char

        if current_token.lower() == 'log':
            self.advance()
            return Token(TokenType.LOG)
        elif current_token.lower() == 'rad':
            self.advance()
            return Token(TokenType.RADICAL)
        elif current_token.lower() == 'sin':
            self.advance()
            return Token(TokenType.SIN, current_token)
        elif current_token.lower() == 'cos':
            self.advance()
            return Token(TokenType.COS)
        elif current_token.lower() == 'tan':
            self.advance()
            return Token(TokenType.TAN)
        else:
            raise Exception(f"Illegal character '{current_token}'")
