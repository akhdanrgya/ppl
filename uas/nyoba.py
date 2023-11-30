def minion_game(string):
    # your code goes here
    vowel = 'AEIOU'
    vnum = 0
    cnum = 0
    n = len(string)
    
    for i, c in enumerate(string):
        print(i,c,string)
        if c in vowel:
            vnum += n - i
        else:
            cnum += n - i

    if vnum == cnum:
        print("Draw")
    elif vnum > cnum:
        print("Kevin " + str(vnum))
    else:
        print('Stuart ' + str(cnum))
    
    print(n)
    print(i)
    print(c)

minion_game("banana")