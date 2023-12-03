def main();

  content = ""
  with open('example.optxt', 'r') as file:
    content = file.read()

print(content)

main()
