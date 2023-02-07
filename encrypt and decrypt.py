alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(plain_text,shift_amount,new_direction):
    celi = ""
    if new_direction =="decode":
        shift_amount *= -1
    for letter in plain_text:
        position=alphabet.index(letter)
        new_pos=position+shift_amount
        celi += alphabet[new_pos]
    print(f"The {new_direction}d value is: {celi}")
        

caesar(plain_text=text,shift_amount=shift,new_direction=direction)