def encrypt(string, key):
    cipher = ''
    for char in string:
        if char.isupper():
            cipher = cipher + chr(((ord(char) - 65) +  key) % 26 + 65) 
        elif char.islower():
            cipher = cipher + chr(((ord(char) - 97) + key) % 26 + 97)
        else:
            cipher += char
    return cipher
def decrypt(string, key):
    cipher = ''
    for char in string:
        if char.isupper():
            cipher = cipher + chr(((ord(char) - 65) -  key) % 26 + 65) 
        elif char.islower():
            cipher = cipher + chr(((ord(char) - 97) - key) % 26 + 97)
        else:
            cipher += char
    return cipher
    
print("Ceaser cipher")
print("Krishna Tikarya")
print(" ")
text = input("Enter the string: ")
s = int(input("Enter the key: "))
print("After encryption: ",encrypt(text,s))
print("After decryption: ", decrypt(text,s))