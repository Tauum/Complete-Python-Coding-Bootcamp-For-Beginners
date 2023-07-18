# classes


class Character:
    # attributes
    title = ""
    names = []
    items = {}
    languages = []
    position = ()
    health = 100

    # initializer
    def __init__(self, title, names, items, languages, position):
        self.title = title
        self.names = names
        self.items = items
        self.languages = languages
        self.position = position

    # behaviour
    def change_health(self, health):
        if self.health <= 0 or health <= 0:
            print(f"Health > {health} <character is dead")
        self.health = health
        print(f"Characters health is now {health}")
        return

    def learn_language(self, language):
        if language is None or language == "":
            print("Cannot learn - not a valid language")
            return
        for element in self.languages:
            if element.capitalize() == language.capitalize():
                print(f"Language > {language} < is already known")
                return
        self.languages.append(language.capitalize())
        print(f"Language > {language} < was learned")
        return

    def unlearn_language(self, language):
        if language is None or language == "":
            print("Cannot unlearn - not a valid language")
        for element in self.languages:
            if element.capitalize() == language.capitalize():
                self.languages.remove(language.capitalize())
                print(f"Language > {language} < was unlearned")
                return
        print(f"Language > {language} < is not currently known")

    def set_title(self, title):
        if title is not None and title != "":
            self.title = title
        return

    def print_self(self):
        print(f"\nTitle: {self.title}"
              f"\nNames: {self.names}"
              f"\nItems: {self.items}"
              f"\nLanguages: {self.languages}"
              f"\nPosition: {self.position}")
        return
