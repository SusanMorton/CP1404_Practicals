import wikipedia


def main():
    userinput = input("Type in a page title or wiki search phrase: ")
    while userinput != "":
        try:
            print(wikipedia.page(userinput))
            print(wikipedia.summary(userinput))
            url = wikipedia.page(userinput)
            print(url.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        userinput = input("Type in a page title or wiki search phrase: ")


main()