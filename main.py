while True:
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    encrypt = input("Enter a clear message:").lower()
    key = int(input("Please enter a key ( number from 1-25): "))
    encrypted = ""
    for letter in encrypt:
        position = alphabet.find(letter)
        newPosition = position + key
        if letter in alphabet:
            if letter in alphabet[-1:-key-1:-1]:
                encrypted=encrypted + alphabet[position + key - len(alphabet)]
            else:
                encrypted = encrypted + alphabet[newPosition]
        else:
           encrypted = encrypted + letter
    print("Your cipher is: ", encrypted)



