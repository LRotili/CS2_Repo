from math import factorial as fct       

def indall(k, N):
    P = 2**k
    PHet = 0                                                                
    for gen in range(N, P + 1):                                                     
        prob = (fct(P) /(fct(gen) * fct(P - gen))) * (0.25**gen) * (0.75**(P - gen))                                                        
        PHet += prob                                                        
        
    return PHet


print(indall(7,35))