def main():

  content = ""
  with open('example.optxt', 'r') as file:
    content = file.read()
    #
    # Lexer
    # 

lex = lexer.Lexer(content)
tokens = lex.tokenize()

main()
