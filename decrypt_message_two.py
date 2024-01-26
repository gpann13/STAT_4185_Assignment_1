encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()


backward = len(encrypted_message)-2
char = 0
decrypted_message = ""

while char < len(encrypted_message):
    decrypted_message += encrypted_message[char]
    decrypted_message += encrypted_message[backward]
    char += 2
    backward -= 2

print(decrypted_message)

