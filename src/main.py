def main();

  content = ""
  with open('main.optxt', 'r') as file:
    content = file.read()

print(content)

main()
