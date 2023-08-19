import re

# Definir una lista de palabras reservadas
reserved_words = {
    'if': 19,
    'while': 20,
    'return': 21,
    'else': 22,
    'int': 4,
    'float': 4,
    'void': 4
}

# Función para verificar si una cadena es un número entero
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Función para verificar si una cadena es un número real
def is_real(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Función para analizar la cadena de entrada
def lexer(input_string):
    tokens = input_string.split()
    token_list = []

    for token in tokens:
        if token in reserved_words:
            token_list.append((reserved_words[token], token))
        elif is_integer(token):
            token_list.append((1, token))
        elif is_real(token):
            token_list.append((2, token))
        elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):  # Identificadores
            token_list.append((0, token))
        elif token in ['+', '-']:
            token_list.append((5, token))
        elif token in ['*', '/']:
            token_list.append((6, token))
        elif token in ['<', '<=', '>', '>=']:
            token_list.append((7, token))
        elif token == '||':
            token_list.append((8, token))
        elif token == '&&':
            token_list.append((9, token))
        elif token == '!':
            token_list.append((10, token))
        elif token in ['==', '!=']:
            token_list.append((11, token))
        elif token == ';':
            token_list.append((12, token))
        elif token == ',':
            token_list.append((13, token))
        elif token == '(':
            token_list.append((14, token))
        elif token == ')':
            token_list.append((15, token))
        elif token == '{':
            token_list.append((16, token))
        elif token == '}':
            token_list.append((17, token))
        elif token == '=':
            token_list.append((18, token))
        else:
            token_list.append((3, token))  # Por defecto, tratarlo como una cadena

    token_list.append((23, '$'))  # Agregar token de fin de cadena

    return token_list


if __name__ == "__main__":
    input_string = input("Ingrese una cadena de texto: ")
    tokens = lexer(input_string)
    for token_type, token_value in tokens:
        print(f'Token de tipo {token_type}: {token_value}')
