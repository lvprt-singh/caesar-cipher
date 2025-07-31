def encrypt(sentence, key):
    text = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in sentence:
        if char.isalpha():
            shift = text.index(char.lower())%26 + key
            value = text[shift]
            encrypted += value
        else: 
            encrypted += char
    return encrypted

def decrypt(sentence, key):
    text = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    for char in sentence:
        if char.isalpha():
            shift = text.index(char.lower())%26 - key
            value = text[shift]
            decrypted += value
        else: 
            decrypted += char
    return decrypted

run_time = 0
while run_time < 3:
    direction = input("What do you want to perform: ")

    if direction.lower() == 'encrypt':
        text_in = input('Enter a line to encrypt: ')
        key_in = int(input('Enter your secret password: '))
        output = encrypt(text_in,key_in)
        print(output)

    elif direction.lower() == 'decrypt':
        text_in = input('Enter a line to decrypt: ')
        key_in = int(input('Enter your secret password: '))
        output = decrypt(text_in,key_in)
        print(output)
        
    else: 
        run_time += 1
        print('wrong input, try again')
        
    print(f'Number of tries left: {3 - run_time}')

    if run_time == 3:
        print('exiting now')
        break