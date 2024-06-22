alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
            , 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from logo import logo
def caesar():
    def encrypt(plain_text, shift_number):
        cipher_text = ""
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_number
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += letter
        print(f"The encoded text is {cipher_text}")

    def decrypt(cipher_text, shift_number):
        plain_text = ""
        for letter in cipher_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_number
                new_letter = alphabet[new_position]
                plain_text += new_letter
            else:
                cipher_text += letter
        print(f"The decoded text is{plain_text}")

    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        print("Goodbye")

should_end = False
while not should_end:
    caesar()
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
