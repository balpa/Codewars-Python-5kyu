def pig_it(text):
    word = text.split()
    ay = [f"{x[1:]}{x[0]}"+"ay" for x in word]
    ayString = ' '.join(ay)
    aysplit = ayString.split()
    QM = "?"
    EX = "!"
    print(aysplit)
    for x in range(len(aysplit)):
        if QM in aysplit[x]:
            aysplit[x] = QM
            ayString = aysplit
        elif EX in aysplit[x]:
            aysplit[x] = EX
            ayString = aysplit
    return ' '.join(aysplit)
