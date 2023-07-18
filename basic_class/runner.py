from basic_class.classes.character import Character

print("class init")

character1 = Character(
    title="Esquire",
    names=["Fredrick", "Daniels"],
    items={"Book of Knowledge": 1, "Water": 2},
    languages=["English"],
    position=(0, 0)
)

print(character1)
print(character1.print_self())

character1.learn_language("french")
character1.learn_language("english")
character1.unlearn_language("english")


print(character1.print_self())