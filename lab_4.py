Text1=[]
print("Введите текст (каждое предложение в новой строке)")
while True:
    k = input()
    if (k==""):
        break
    else:  Text1.append(k)
print("Введенный текст")
print(Text1)
Text2=[]
for i in Text1:
    pred=str(i)
    newpred=""
    i=0
    k1=0
    while (i<len(pred)):
        if (pred[i+1]==pred[i] and pred[i]!=''):
            p=pred[i]
            k1=0
            while(pred[i]==p and pred[i]!=''):
                i=i+1
                k1=k1+1
                if(i>=len(pred)):
                    break
            newpred=newpred+p+str(k1)
        else:
            newpred=newpred+pred[i]
            i=i+1
            if (pred[i] == pred[len(pred)-1]):
                newpred = newpred + pred[i]
                break

    Text2.append(newpred)
print("")
print("Результат")
print(Text2)
