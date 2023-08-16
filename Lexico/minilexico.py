class TokenType:
    IDENTIFIER = 1
    REAL_NUMBER = 2
    INVALID = 3

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, input):
        self.input = input
        self.current_position = 0

    def get_next_token(self):
        while self.current_position < len(self.input) and self.input[self.current_position].isspace():
            self.current_position += 1

        if self.current_position >= len(self.input):
            return Token(TokenType.INVALID, "")

        current_char = self.input[self.current_position]
        if current_char.isdigit():
            if self.current_position + 1 < len(self.input) and self.input[self.current_position + 1].isalpha():
                invalid_text = current_char
                self.current_position += 1
                while self.current_position < len(self.input) and self.input[self.current_position].isalnum():
                    invalid_text += self.input[self.current_position]
                    self.current_position += 1
                return Token(TokenType.INVALID, invalid_text)
            else:
                return self.extract_real_number()
        elif current_char.isalpha():
            return self.extract_identifier()
        else:
            return Token(TokenType.INVALID, "")

    def extract_identifier(self):
        identifier = ""
        while self.current_position < len(self.input) and (self.input[self.current_position].isalnum()):
            identifier += self.input[self.current_position]
            self.current_position += 1
        return Token(TokenType.IDENTIFIER, identifier)

    def extract_real_number(self):
        number = ""
        has_decimal_point = False

        while self.current_position < len(self.input):
            current_char = self.input[self.current_position]
            if current_char.isdigit():
                number += current_char
            elif current_char == '.':
                if has_decimal_point:
                    break
                number += current_char
                has_decimal_point = True
            else:
                break
            self.current_position += 1

        if number == ".":
            return Token(TokenType.INVALID, "")

        return Token(TokenType.REAL_NUMBER, number)

def main():
    input_text = input("Ingresa la cadena de texto: ")
    lexer = Lexer(input_text)
    
    while True:
        token = lexer.get_next_token()

        if token.type == TokenType.IDENTIFIER:
            print("Identificador:", token.value)
        elif token.type == TokenType.REAL_NUMBER:
            print("Numero real:", token.value)
        elif token.type == TokenType.INVALID:
            if token.value:
                print("Token invalido:", token.value)
            else:
                print(" ")

        if not token.value:
            break

if __name__ == "__main__":
    main()