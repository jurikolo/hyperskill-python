available_formatters = ["plain", "bold", "itelic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
while True:
    user_input = input("Choose a formatter:")
    if user_input == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    elif user_input == "!done":
        break
    elif user_input in available_formatters:
        pass
    else:
        print("Unknown formatting type or command")