while True:
    alphabet = {"eng": "abcdefghijklmnopqrstuvwxyz",
                "ukr": "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя",
                "nums": "0123456789"
                }
    encrypt = input("Enter a clear message: ").lower()
    encrypted = ""
    for letter in encrypt:
        if letter in alphabet["eng"]:
            position = alphabet["eng"].find(letter) + 1
            if letter in alphabet["eng"][-1]:
                encrypted = encrypted + alphabet["eng"][0]
            else:
                encrypted = encrypted + alphabet["eng"][position]
        elif letter in alphabet["ukr"]:
            position = alphabet["ukr"].find(letter) + 1
            if letter in alphabet["ukr"][-1]:
                encrypted = encrypted + alphabet["ukr"][0]
            else:
                encrypted = encrypted + alphabet["ukr"][position]
        elif letter in alphabet["nums"]:
            position = alphabet["nums"].find(letter) + 1
            if letter in alphabet["nums"][-1]:
                encrypted = encrypted + alphabet["nums"][0]
            else:
                encrypted = encrypted + alphabet["nums"][position]
        else:
            encrypted = encrypted + letter
    print(encrypted)

