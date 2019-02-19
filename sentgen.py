import random
import numpy as np

def alg(N=5):
    
    str1=['the','his','their','an']
    str2=['enthusiastic','active','efficient','archaic']
    str3=['boy','cat','computer','machine']
    str4=['eats','chases','makes','produces']
    str5=['chocolate','mice','calculations','tools']
    
    #Vstr=[str1,str2,str3,str4,str5]
    block1=random.choice(str1,N)
    block2=random.choice(str2,N)
    block3=random.choice(str3,N)
    block4=random.choice(str4,N)
    block5=random.choice(str5,N)
    #sentgroup=np.zeros(N)
    #for i in range(0,N):
    #    sentgroup[i] = random.choice(str1)+' '+random.choice(str2)+' '+random.choice(str3)+' '+random.choice(str4)
    sentce=np.zeros(N)
    for i in range(0,N):
        sentce[i]=block1[i]+' '+block2[i]+' '+block3[i]+' '+block4[i]+' '+block5[i]

        
        #sentce[ = random.choice(str1)+' '+random.choice(str2)+' '+random.choice(str3)+' '+random.choice(str4)+' '+random.choice(str5)
        #sentce2 = random.choice(str1)+' '+random.choice(str2)+' '+random.choice(str3)+' '+random.choice(str4)+' '+random.choice(str5)
    
    return sentce

