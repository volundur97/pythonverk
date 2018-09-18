word = input("Enter a word: ")
the_vowel = ["a","e","i","o","u"]
the_consonant = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","z"]

while word != ".":
    orð = word
    if word[0] in the_vowel:
        orð = word + "yay"

    else:
        for i in orð:
            if orð[0] not in the_vowel:
                orð = orð[1::] + orð[0]
        
        orð += "ay"
    print(orð)
    word= input("Enter a word: ")