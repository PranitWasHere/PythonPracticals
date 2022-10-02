import wikipedia


def main():
    while True:
        title = input("Enter a page title: ")
        if not title:
            print("Thank you")
            break

        try:
            sm = wikipedia.summary(title)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        pg = wikipedia.page(title, auto_suggest=False)
        print(f"Title: {pg.title}\nURL: {pg.url}\nSummary: {sm}")


if __name__ == '__main__':
    main()