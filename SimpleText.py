while True:
    print("Please enter your text here: (press enter when you're finished)")
    text = input("")

    print("")
    print("What do you want to do now?")
    print("-----CHOICES-----")
    print("1 - Copy (requires pyperclip)")
    print("2 - Turn it into a HTML File")
    print("3 - Save it as a .txt file")
    print("-----------------")

    print("")
    choice = input("Enter your choice here: ")

    if choice == "1":
        import pyperclip

        pyperclip.copy(text)

        print("Text has been now copied!")
        print("")

    if choice == "2":
        with open ('YourHTML.html', 'w') as f:
            f.write('<html> <head> <title>Your Text</title> </head> <body> <font size=5> <p>' + text + '</p> </font> </body> </html>')

        print("HTML File Generated!")
        print("")

    if choice == "3":
        with open ('YourTextFile.txt', 'w') as t:
            t.write(text)
        print(".txt file generated!")
        print("")
