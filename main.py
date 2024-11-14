word = "hippopotamus"

if len(word)%2 > 0:
    symbol_number = int(len(word)/2+1)
    print(word[symbol_number])
else:
    symbol_number = int(len(word)/2)
    print(word[symbol_number-1] + word[symbol_number])



