def get_text():
    while True:
        text = input('Text:')
        if text != "":
            return text


def get_header_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 7):
                return level
            else:
                print("The level should be within the range of 1 to 6")
        except Exception:
            pass


available_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line"]
markdown_text = ""
while True:
    if markdown_text != "":
        print(markdown_text)
    user_input = input("Choose a formatter: ")
    if user_input == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif user_input == "!done":
        break
    elif user_input in available_formatters:
        if user_input == "plain":
            markdown_text += get_text()
        elif user_input == "bold":
            markdown_text += f"**{get_text()}**"
        elif user_input == "italic":
            markdown_text += f"*{get_text()}*"
        elif user_input == "inline-code":
            markdown_text += f"`{get_text()}`"
        elif user_input == "header":
            level = get_header_level()
            text = input("Text:")
            markdown_text += level * "#" + f" {text}\n"
        elif user_input == "link":
            label = input("Label:")
            url = input("URL:")
            markdown_text += f"[{label}]({url})"
        elif user_input == "new-line":
            markdown_text += "\n"
    else:
        print("Unknown formatting type or command")
