import re
import collections
import pickle

global Total_Keys
Total_Keys=0
global Total_suggested_bigram_Keys
Total_suggested_Keys=0
global Total_suggested_Unigram
Total_suggested_Unigram=0
global Total_suggested_Trigram
Total_suggested_Trigram=0
global Previous_bigram
Previous_bigram='<s>'
global Previous_Trigram
Previous_Trigram='</s> <s>'
global current_word
current_word=""

Urdu_Sentences = open("Corpus.txt", encoding = "utf-16").read()

Urdu_Sentences = re.sub(r'[^\w\s]*_*','',Urdu_Sentences)

#print(Urdu_Sentences)
#Urdu_SentencesCOPY = re.split(r'[تھا|گی|گئے|گیا|ڈالا|تھی|ہوں|گا|تھے|سکتی|ہیں|گے|ہے]',Urdu_SentencesCOPY)
#print(Urdu_SentencesCOPY)

Given=Urdu_Sentences.split("\n")
#print(Given)
list_s1=[]
def Addstart_and_End(Sentences):
    Sentences=Sentences.lstrip()
    Sentences=Sentences.rstrip()
    
    list_s1.append('<s>')
    for word in Sentences.split():
        list_s1.append(word)
    list_s1.append('</s>')
    #print(list_s1)
    result= ' '.join(list_s1)
    #print(result)
    
    file = open("startEndAdded.txt","w",encoding = "utf-16")
    file.write(result)
    #print(result)



count=len(Given)
i=0
while(i < count):
    Addstart_and_End(Given[i])
    #print(Given[i])
    i+=1

startEndAdded = open("startEndAdded.txt", encoding = "utf-16").read()
startEndAdded=startEndAdded.split()




UnigramCont = collections.Counter()
for word in startEndAdded:
    #print(word)
    UnigramCont[word] =UnigramCont[word]+1
print(UnigramCont)
n=len(startEndAdded)
UnigramProb = collections.Counter()
for word,k in UnigramCont.items():
    UnigramProb[word]=UnigramCont[word]/n
print(UnigramProb)

#This was storing them into a file but i wasn't able to get them as counter
#with open("unigramprob.txt",encoding='utf-16', mode='w') as f:
#    for k,v in  UnigramProb.items():
#        f.write( "{} {}\n".format(k,v) )
        
with open('UnigramProb', 'wb') as outputfile:
     pickle.dump(UnigramProb, outputfile)
     
#with open('UnigramProb', 'rb') as UnigramProb:
#     print(pickle.load(UnigramProb))

i=0
Bigram_S1=[]
Bigram_S1_Final=[]
while(i < len(startEndAdded)):
    if(i==len(startEndAdded)-1):
        break
    
    else:
        a=startEndAdded[i]
        Bigram_S1.append(a)
        i+=1
        b=startEndAdded[i]
        Bigram_S1.append(b)
        #print(Bigram_S1)
        result= ' '.join(Bigram_S1)
        Bigram_S1_Final.append(result)
        result=""
        Bigram_S1=[]
print("\nBiGram are: ",Bigram_S1_Final)
BigramCont = collections.Counter()
for word in Bigram_S1_Final:
    #print(word)
    BigramCont[word] += 1
#print("Bigram Count is: ",BigramCont)
#
BigramProb = collections.Counter()
for word2,k2 in BigramCont.items():
    divisor=(word2.partition(' ')[0])
    divisorCont = collections.Counter()
    for word in divisor:
        for word,k in UnigramCont.items():
            if(divisor==word):
                #divisorCont[divisor]+=1
                break
            
    #print(divisor, "\t",k,"\t",word2,"\t", k2)
    BigramProb[word2]=BigramCont[word2]/k
print("Bigram Probabilites are: ",BigramProb)
#file = open("bigramprob.txt","w",encoding = "utf-16")
#file.write(BigramProb)
#with open("bigramprob.txt",encoding='utf-16', mode='w') as f:
#    for k,v in  BigramProb.items():
#        f.write( "{} {}\n".format(k,v) )
with open('BigramProb', 'wb') as outputfile:
     pickle.dump(BigramProb, outputfile)
#


#Trigram Words Model
i=0
Trigram_S1=[]
Trigram_S1_Final=[]
while(i < len(startEndAdded)):
    if(i==len(startEndAdded)-2):
        break
    
    else:
        a=startEndAdded[i]
        Trigram_S1.append(a)
        i+=1
        b=startEndAdded[i]
        Trigram_S1.append(b)
        i+=1
        c=startEndAdded[i]
        Trigram_S1.append(c)
        #print(Bigram_S1)
        result= ' '.join(Trigram_S1)
        Trigram_S1_Final.append(result)
        result=""
        i-=1
        Trigram_S1=[]
print("\nTriGram are: ",Trigram_S1_Final)
TrigramCont = collections.Counter()
for word in Trigram_S1_Final:
    #print(word)
    TrigramCont[word] += 1
print("Trigram Count is: ",TrigramCont)

#Calculating Trigram Probability
TrigramProb = collections.Counter()
for word3,k3 in TrigramCont.items():
    word4=word3.split()
    divisor=word4[0:2]
    divisor=' '.join(divisor)
    #print(divisor)
    divisorCont = collections.Counter()
    for word in divisor:
        
        for word,k in BigramCont.items():
            if(divisor==word):
                #divisorCont[divisor]+=1
                break
            
    #print(divisor, "\t",k,"\t",word3,"\t", k3)
    TrigramProb[word3]=TrigramCont[word3]/k
print("Triigram Probabilites are: ",TrigramProb)

#with open("trigramprob.txt",encoding='utf-16', mode='w') as f:
#    for k,v in  TrigramProb.items():
#        f.write( "{} {}\n".format(k,v) )
with open('TrigramProb', 'wb') as outputfile:
     pickle.dump(TrigramProb, outputfile)

#Urdu_Sentencess = open("startEndAdded.txt", encoding = "utf-8-sig").read()
#ss1 = set(Urdu_Sentencess) #yahan union krna hai k sirf unique iss me hn taky unigram count kr sakon 