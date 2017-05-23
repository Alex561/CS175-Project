import colors as ColorDict
def QuantitiveEval(dif):
    sum=0
    for i in range(len(dif)):
        sum+=dif[i]
    return sum/len(dif)
    
    
