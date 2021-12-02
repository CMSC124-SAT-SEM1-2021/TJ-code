import traceback

lexemes = []
unknown = ["+", "-", "*", "/", "(", ")", "=", "!", ";"]
keyword = ["if", "then", "elif", "else", "for", "while", "in", "int", "float", "double", "char",
           "string", "do"]
dontMindElements = [" ", "\n", "\t", "\v", "\f", "\r"]

# -------------------------------------------------------------------------
# ------------------------ getChar() --------------------------------------
# -------------------------------------------------------------------------

def getChar():
    try:
        text = open("input.txt", "r")
        lexCount = 0
        is_Digit = False


        for line in text:
            lex = ""        # temp store string here to pass on addChar
            for character in line:
                if character.isalpha() == True:

                    # in case a digit is immediately followed by a letter in lex
                    if lex: # if lex is not empty
                        if lex[len(lex)-1].isdigit() & lex[0].isdigit(): # if first and last characters are digit
                            addChar(lex)  # add the existing lex to the array
                            lexCount = lexCount + 1
                            lex = ""

                    lex = lex + character # proceeds to add letter to lex

                elif character.isdigit() == True:

                    lex = lex + character
                else:
                    if lex:         # if the lex is not empty
                        addChar(lex)    # add the existing lex to the array
                        lexCount = lexCount + 1
                        lex = ""
        
                    if character not in dontMindElements:
                        addChar(character)

        addChar(lex)  # add the last lex
        lexCount = lexCount + 1
        lex = ""

        text.close()
    except Exception:
        traceback.print_exc()

# -------------------------------------------------------------------------
# ------------------------ lookup() --------------------------------------
# -------------------------------------------------------------------------

def lookup(lexeme):
    unknownNames = {
        "+": "PLUS_OP",
        "-": "MINUS_OP",
        "/": "DIV_OP",
        "(": "L_PAREN",
        ")": "R_PAREN",
        "=": "ASSIGN_OP",
        "!": "LOGICAL_NOT",
        ";": "SEMI COLON",
    }
    return unknownNames[lexeme]

# -------------------------------------------------------------------------
# ------------------------ addChar() --------------------------------------
# -------------------------------------------------------------------------

def addChar(lexeme):
    lexemes.append(lexeme)

# def addChar(lexeme, token):


# -------------------------------------------------------------------------
# ------------------------ main fcn ---------------------------------------
# -------------------------------------------------------------------------
getChar()
for lexeme in lexemes:
    if lexeme in unknown:
        print(lexeme + " " + lookup(lexeme))
    elif lexeme[0].isalpha() == True:
        if lexeme in keyword:
            print(lexeme + " KEYWORD")
        else:
            print(lexeme + " IDENTIFIER")
    elif lexeme[0].isdigit() == True:
        print(lexeme + " INT LITERAL")
    else:
        print(lexeme + " INVALID")
