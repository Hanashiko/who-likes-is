def likes(names: list[str]):
    length: int = len(names)
    if length == 0:
        return "no one likes this"
    elif length == 1:
        return f"{names[0]} likes this"
    elif length == 2:
        return f"{names[0]} and {names[1]} like this"
    elif length == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif length > 3:
        return f"{names[0]}, {names[1]} and {len(names[2:])} others like this"

print(likes(["Alex", "Jacob", "Mark", "Max"] ))
