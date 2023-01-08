#get word from user
word = input()
password = ""

#replaces certain characters with new characters to make a new word that can be used for a strong password
password = word.replace("i", "1");
password = password.replace("a", "@"):
password = password.replace("m", "M");
password = password.replace("B", "8");
password = password.replace("s", "$");

print(password + "!")
