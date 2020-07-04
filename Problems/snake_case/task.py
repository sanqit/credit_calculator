camel_word = input()

snake_word = ""

for letter in camel_word:
    if letter.isupper():
        snake_word += "_"
        snake_word += letter.lower()
    else:
        snake_word += letter

print(snake_word)
