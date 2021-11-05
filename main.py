from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
symbols = ['+', '-', '_', '(', ')', '*', '&', '^', '%', '$', '#', '@', '!', ',', ',', '/']


def caesar(texts, shifts, directions):
    def encrypt(plain_text, shift_amount):
        encrypted_text = ""
        encrypted_text_list = []
        for letter in plain_text:
            if letter == " " or letter in symbols or letter.isdigit() == True:
                encrypted_text_list.append(letter)
            else:
                encrypted_letter_index = alphabet.index(letter) + shift_amount
                encrypted_text_list.append(alphabet[encrypted_letter_index])
        for items in encrypted_text_list:
            encrypted_text += items
        return f"The encoded text is {encrypted_text}"

    def decrypt(encoded_text, shift_amount):
        decrypted_text = ""
        decrypted_text_list = []
        for letter in encoded_text:
            if letter == " " or letter in symbols or letter.isdigit() == True:
                decrypted_text_list.append(letter)
            else:
                decrypted_text_index = alphabet.index(letter) - shift_amount
                decrypted_text_list.append(alphabet[decrypted_text_index])
        for items in decrypted_text_list:
            decrypted_text += items
        return f"The decoded text is {decrypted_text} "

    if directions == "encode":
        return encrypt(texts, shifts)
    elif directions == "decode":
        return decrypt(texts, shifts)


print(logo)

flag = True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(caesar(texts=text, shifts=shift, directions=direction))
    ask_user = input("would you like to continue using the program? Types yes or no ").lower()
    if ask_user == "yes":
        flag = True
    elif ask_user == "no":
        flag = False
