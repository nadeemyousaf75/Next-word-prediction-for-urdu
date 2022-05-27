# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:46:58 2018

@author: NAdim
"""

import tkinter as tk
import collections
from tkinter import messagebox
import pickle

#Model
with open('UnigramProb', 'rb') as UnigramProb:
     #print(pickle.load(UnigramProb))
     UnigramProb=pickle.load(UnigramProb)
with open('BigramProb', 'rb') as BigramProb:
     #print(pickle.load(BigramProb))
     BigramProb=pickle.load(BigramProb)
with open('TrigramProb', 'rb') as TrigramProb:
     #print(pickle.load(TrigramProb))
     TrigramProb=pickle.load(TrigramProb)

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
global previousChar
previousChar=""
global CountSpaces
CountSpaces=0


#UnigramCont = collections.Counter()
#for word in txt:
#    #print(word)
#    UnigramCont[word] =UnigramCont[word]+1
#print(UnigramCont)
#n=len(txt)
#UnigramProb = collections.Counter()
#for word,k in UnigramCont.items():
#    UnigramProb[word]=UnigramCont[word]/n
#print(UnigramProb)
##for word,k in UnigramCont.items():
##    print(k,word)

#i=0
#Bigram_S1=[]
#Bigram_S1_Final=[]
#while(i < len(txt)):
#    if(i==len(txt)-1):
#        break
#    
#    else:
#        a=txt[i]
#        Bigram_S1.append(a)
#        i+=1
#        b=txt[i]
#        Bigram_S1.append(b)
#        #print(Bigram_S1)
#        result= ' '.join(Bigram_S1)
#        Bigram_S1_Final.append(result)
#        result=""
#        Bigram_S1=[]
#print("\nBiGram are: ",Bigram_S1_Final)
#BigramCont = collections.Counter()
#for word in Bigram_S1_Final:
#    #print(word)
#    BigramCont[word] += 1
#print("Bigram Count is: ",BigramCont)
#
#BigramProb = collections.Counter()
#for word2,k2 in BigramCont.items():
#    divisor=(word2.partition(' ')[0])
#    divisorCont = collections.Counter()
#    for word in divisor:
#        for word,k in UnigramCont.items():
#            if(divisor==word):
#                #divisorCont[divisor]+=1
#                break
#            
#    #print(divisor, "\t",k,"\t",word2,"\t", k2)
#    BigramProb[word2]=BigramCont[word2]/k
#print("Bigram Probabilites are: ",BigramProb)
#    
#    #print(word.partition(' ')[0])  <s> nadeem this is how you can get <s>
#    
#    #BigramCont[word]=BigramCont[word]/k
#
##Trigram Words Model
#i=0
#Trigram_S1=[]
#Trigram_S1_Final=[]
#while(i < len(txt)):
#    if(i==len(txt)-2):
#        break
#    
#    else:
#        a=txt[i]
#        Trigram_S1.append(a)
#        i+=1
#        b=txt[i]
#        Trigram_S1.append(b)
#        i+=1
#        c=txt[i]
#        Trigram_S1.append(c)
#        #print(Bigram_S1)
#        result= ' '.join(Trigram_S1)
#        Trigram_S1_Final.append(result)
#        result=""
#        i-=1
#        Trigram_S1=[]
#print("\nTriGram are: ",Trigram_S1_Final)
#TrigramCont = collections.Counter()
#for word in Trigram_S1_Final:
#    #print(word)
#    TrigramCont[word] += 1
#print("Trigram Count is: ",TrigramCont)
#
##Calculating Trigram Probability
#TrigramProb = collections.Counter()
#for word3,k3 in TrigramCont.items():
#    word4=word3.split()
#    divisor=word4[0:2]
#    divisor=' '.join(divisor)
#    #print(divisor)
#    divisorCont = collections.Counter()
#    for word in divisor:
#        
#        for word,k in BigramCont.items():
#            if(divisor==word):
#                #divisorCont[divisor]+=1
#                break
#            
#    #print(divisor, "\t",k,"\t",word3,"\t", k3)
#    TrigramProb[word3]=TrigramCont[word3]/k
#print("Triigram Probabilites are: ",TrigramProb)



""" Lang Model done next is Interface """

root = tk.Tk()
root.geometry('900x600')
root.title("Word Predictor")

#input_usr2ap={}
input_usr2ap=""
global previous_word
previous_word=""
def test(event):
    screen = user_input.get("1.0",'end-1c')
    screen= screen.split()
        
    global Total_Keys
    global Previous_bigram
    global current_word
    global Previous_Trigram
    global CountSpaces
    
#        if(event.char == str):
#            input_usr2=event.string
#            
#        else:
    if(event.widget == user_input):
        if(event.char !=""):
            Total_Keys+=1
        #print("Total keys with space",Total_Keys)
        
        if(event.char ==" "):
            CountSpaces+=1
        #print("Only spaces keys",CountSpaces)
        input_usr2=event.char
        global previousChar
        previousChar=input_usr2
        current_word=current_word+input_usr2
        #print("here is current",current_word)
        global input_usr2ap
        input_usr2ap=input_usr2ap+input_usr2
        input_usr2ap.split()
        inputuser3=input_usr2ap.split()
        #print("user entered character",inputuser3)
        #print(Total_Keys)
        #input_usr=input_usr.split()
        radiovalue=var.get()
        #sugg_string.set(radiovalue)
        if(radiovalue==1):
            if(input_usr2==" "):
                suggestion=suggestion_of_Unigram(UnigramProb,input_usr2)
                if(len(suggestion)==0):
                    #print("here")
                    listBox.delete(0, tk.END)
                    listBox.insert(tk.END, "No Match")
                    #sugg_string.set("No Match")
                   
                  
                else:
                        listBox.delete(0, tk.END)
                        for word in suggestion:
                            listBox.insert(tk.END, word)
                       
            else:
                #sugg_string.set("Unigram")
                #print("here 3")
                
                #print(inputuser3)
                n=len(inputuser3)
                Unigrams=inputuser3[n-1:n+1]
                Unigrams=' '.join(Unigrams)
                print(Unigrams)
                #btn4_text.set(Unigrams)
                suggestion=suggestion_of_Unigram(UnigramProb,Unigrams)
                if(len(suggestion)==0):
                    listBox.delete(0, tk.END)
                    #listBox.insert(0,"nadeem")
                    listBox.insert(tk.END, "No Match")
               
                else:
                        listBox.delete(0, tk.END)
                        for word in suggestion:
                            listBox.insert(tk.END, word)
                        
            
#            
            #suggestion=suggestion_of_bigram(BigramProb,bigrams)
        elif(radiovalue==2):
            #sugg_string.set("Bigram")
            #Previous_bigram=suggestion
            #n=len(inputuser3
            if(input_usr2==" "):
                    input_usr = user_input.get("1.0",'end-1c')
                    input_usr=input_usr.split()
                    n=len(input_usr)
                    Previous_bigram=input_usr[n-1:n+1]
                    Previous_bigram=' '.join(Previous_bigram)
#                    Previous_bigram=current_word
                    current_word=""
#                    print(Previous_bigram)
#                    inputuser3=' '.join(inputuser3)
#                    inputuser3=inputuser3.split()
#                    n=len(inputuser3)
#                    Previous_bigram=inputuser3[n-1:n+1]
#                    Previous_bigram=' '.join(Previous_bigram)
               
                    #print("check suggestion aya previous me",Previous_bigram)
                    suggestion=suggestion_of_bigram(BigramProb, current_word,Previous_bigram)
                    if(len(suggestion)==0):
                        #print("hereeeee")
                        listBox.delete(0, tk.END)
                        listBox.insert(tk.END, "No Match")
                        #sugg_string.set("No Match")
                       
                      
                    else:
                            listBox.delete(0, tk.END)
                            for word in suggestion:
                                listBox.insert(tk.END, word)
            else:
                
                #print("In else",current_word, "And Previous",Previous_bigram)
                suggestion=suggestion_of_bigram(BigramProb, current_word,Previous_bigram)
                if(len(suggestion)==0):
                        #print("here")
                        listBox.delete(0, tk.END)
                        listBox.insert(tk.END, "No Match")
                        #sugg_string.set("No Match")
                       
                      
                else:
                            listBox.delete(0, tk.END)
                            for word in suggestion:
                                listBox.insert(tk.END, word)
                    
            
            
            
        elif(radiovalue==3):
            if(input_usr2==" "):
                    input_usr = user_input.get("1.0",'end-1c')
                    input_usr=input_usr.split()
                    n=len(input_usr)
                    if(n==1):
                        Previous_Trigram='<s>'
                        temp=input_usr[n-1:n+1]
                        temp=' '.join(temp)
                        Previous_Trigram=Previous_Trigram+" "+temp
                        print("here",Previous_Trigram)
                        
                    else:
                        Previous_Trigram=input_usr[n-2:n+1]
                        Previous_Trigram=' '.join(Previous_Trigram)
                        print(Previous_Trigram)
                    current_word=""

               
                    #print("check suggestion aya previous me",Previous_bigram)
                    suggestion=suggestion_of_Trigram(TrigramProb, current_word,Previous_Trigram)
                    if(len(suggestion)==0):
                        #print("hereeeee")
                        listBox.delete(0, tk.END)
                        listBox.insert(tk.END, "No Match")
                        #sugg_string.set("No Match")
                       
                      
                    else:
                            listBox.delete(0, tk.END)
                            for word in suggestion:
                                listBox.insert(tk.END, word)
            else:
                
                #print("In else",current_word, "And Previous",Previous_bigram)
                suggestion=suggestion_of_Trigram(TrigramProb, current_word,Previous_Trigram)
                if(len(suggestion)==0):
                        #print("here")
                        listBox.delete(0, tk.END)
                        listBox.insert(tk.END, "No Match")
                        #sugg_string.set("No Match")
                       
                      
                else:
                            listBox.delete(0, tk.END)
                            for word in suggestion:
                                listBox.insert(tk.END, word)
           
        else:
            messagebox.showwarning("Error", "Please Select Ngram Model.")

        
        #print(input)
        #string.set("user entered")
    else:
        radiovalue=var.get()
#        word=btn1_text.get()
#        print("here")
#        print(event.widget(button_1.get()))
        input_usr2=listBox.get(tk.ANCHOR)
        input_usr2=''.join(input_usr2)
        #print(input_usr2)
        if(radiovalue==1):
            #print("Here",input_usr2) its the suggestion clicked
            #Adding on Screen
            input_usr = user_input.get('1.0','end-1c')
            input_usr = input_usr.split()
            n=len(input_usr)
            input_usr3 = input_usr[n-1:n+1]
            input_usr3 = ' '.join(input_usr3)
            print("Input user 3",input_usr3)
            #print("Input User 3",input_usr3) #its what user typed for last word
            if(len(input_usr2)!= 0):
            #print(input_usr2)
            #global previousChar
                if(previousChar == " "):
                    insert=input_usr
                    insert=' '.join(insert)
                    #print("space pressed insert",insert)
                    #print(insert)
                    if(len(insert)==0):
                        final=(insert+"" +input_usr2)
                    else:
                        final=(insert+" " +input_usr2)
                  
                    user_input.delete(1.0, "end-1c")
                    user_input.insert("end-1c", final)
                   
                    
                else:
                    insert=input_usr[0:n-len(input_usr3)]
                    insert=' '.join(insert)
                    #print("Without Space Insert",insert)
                    if(len(insert)==0):
                        final=(insert+"" +input_usr2)
                    else:
                        final=(insert+" " +input_usr2)
                  
                    user_input.delete(1.0, "end-1c")
                    user_input.insert("end-1c", final)
            
        
        
        elif(radiovalue==2):
            
                        input_usr = user_input.get("1.0",'end-1c')
                        n=len(input_usr)
                        #print(suggestion)
#                        suggestion=listBox.get(tk.ANCHOR)
#                        suggestion=''.join(suggestion)
#                        print(suggestion)
                        if(len(input_usr2)!= 0):
                            if(len(input_usr)==0):
                                final=(input_usr +"" + input_usr2)
                            elif(len(current_word)!=0):
                                input_usr=input_usr[0:n-len(current_word)]
                                final=(input_usr +"" + input_usr2)
                            elif(previousChar==" "):
                                final=(input_usr +"" + input_usr2)
                                previousChar=""
                            else:
                                final=(input_usr +" " + input_usr2)
                            user_input.delete(1.0, "end-1c")
                            user_input.insert("end-1c", final)
                            
                        Previous_bigram=input_usr2
                        current_word=""
                        if(current_word==""):
                            suggestion=suggestion_of_bigram(BigramProb, current_word,input_usr2)
                            if(len(suggestion)==0):
                                 listBox.delete(0, tk.END)
                                 listBox.insert(tk.END, "No Match")
                                 
                              
                            else:
                                    listBox.delete(0, tk.END)
                                    for word in suggestion:
                                        listBox.insert(tk.END, word)
 
        elif(radiovalue==3):
                        input_usr = user_input.get("1.0",'end-1c')
                        n=len(input_usr)

                        if(len(input_usr2)!= 0):
                            if(len(input_usr)==0):
                                final=(input_usr +"" + input_usr2)
                            elif(len(current_word)!=0):
                                input_usr=input_usr[0:n-len(current_word)]
                                final=(input_usr +"" + input_usr2)
                            elif(previousChar==" "):
                                final=(input_usr +"" + input_usr2)
                                previousChar=""
                            else:
                                final=(input_usr +" " + input_usr2)
                            user_input.delete(1.0, "end-1c")
                            user_input.insert("end-1c", final)
                            
                        Index1=input_usr2
                        indexZero=Previous_Trigram.split()
                        indexZero=indexZero[1]
                        Previous_Trigram=indexZero+" "+Index1
                        print(Previous_Trigram)
                       
                        #print(temp1)
                        current_word=""
                        if(current_word==""):
                            suggestion=suggestion_of_Trigram(TrigramProb, current_word,Previous_Trigram)
                            if(len(suggestion)==0):
                                 listBox.delete(0, tk.END)
                                 listBox.insert(tk.END, "No Match")
                                 
                              
                            else:
                                    listBox.delete(0, tk.END)
                                    for word in suggestion:
                                        listBox.insert(tk.END, word)
                        

def suggestion_of_Unigram(MainUnigram, SearcHUnigram):
    
    sugg = []
    Unigrams=[]
    n=len(SearcHUnigram)
    #print(SearcHBigram)
    if(SearcHUnigram==" "):
        for index in range(0,len(UnigramProb.most_common())):
            if(index>=15):
                break
            else:
                sugg.append(UnigramProb.most_common()[index][0])
        
        return sugg
    else:
        for word2,k2 in MainUnigram.items():
            for index in range(len(word2)):
    #             print(word2[0:n])
    #            word=word3.partition(' ')[0:n]
    #            word=' '.join(word)
                if(word2[0:n] == SearcHUnigram):
                    Unigrams.append(word2)
                else:
                    break
    #            if((word3.partition(' ')[0])==SearcHBigram ):
    #                bigrams.append(word3.partition(' ')[2])
                   
                    
        counter = collections.Counter(Unigrams)
        for index in range(0,len(counter.most_common())):
            if(index>=15):
                break
            else:
                sugg.append(counter.most_common()[index][0])
        
        return sugg
        
def suggestion_of_bigram(MainBigram, currrent,previous):
    
    sugg = []
    bigrams=[]
    bigram_sugg=[]
    #print(SearcHBigram)
    #screen=user_input.get("1.0",'end-1c')
    if(previous=="<s>" and currrent ==""):
        for word3,k3 in BigramProb.items():
                if((word3.partition(' ')[0])=='<s>' ):
                    bigrams.append(word3.partition(' ')[2])
                   
                    
        counter = collections.Counter(bigrams)
        for index in range(0,len(counter.most_common())):
            if(index>=15):
                break
            else:
                sugg.append(counter.most_common()[index][0])
        
        return sugg
  
    elif(currrent==""):
        for word3,k3 in BigramProb.items():
                if((word3.partition(' ')[0])== previous):
                    bigrams.append(word3.partition(' ')[2])
                   
                    
        counter = collections.Counter(bigrams)
        for index in range(0,len(counter.most_common())):
            if(index>=15):
                break
            else:
                sugg.append(counter.most_common()[index][0])
        
        return sugg
    else:
        n=len(currrent)
        for word3,k3 in BigramProb.items():
                if((word3.partition(' ')[0])== previous):
                    bigrams.append(word3.partition(' ')[2])
        bigrams = collections.Counter(bigrams)
        #print(bigrams)
        for word2,k2 in bigrams.items():
            for index in range(len(word2)):
                 if(word2[0:n] == currrent):
                    bigram_sugg.append(word2)
        counter=collections.Counter(bigram_sugg)
        for index in range(0,len(counter.most_common())):
            if(index>=15):
                break
            else:
                sugg.append(counter.most_common()[index][0])
        
        return sugg

def suggestion_of_Trigram(MainTrigram, current , previous):
    
    sugg = []
    Trigrams=[]
    Trigram_sugg=[]
    if(previous=="</s> <s>" and current ==""):
        for word3,k3 in MainTrigram.items():
            word4=word3.split()
            divisor=word4[0:2]
            divisor=' '.join(divisor)
            #print(divisor)
            if(divisor==previous):
                    adder=word4[2:3]
                    adder=' '.join(adder)
                    #print(adder)
                    Trigrams.append(adder)
                   
                    
        counter = collections.Counter(Trigrams)
        #print(counter)
        for index in range(0,len(counter.most_common())):
            if(index>=15):
                break
            else:
                sugg.append(counter.most_common()[index][0])
        
        return sugg
    elif(current==""):
        for word3,k3 in MainTrigram.items():
                word4=word3.split()
                divisor=word4[0:2]
                divisor=' '.join(divisor)
                if(divisor== previous):
                    adder=word4[2:3]
                    adder=' '.join(adder)
                    #print(adder)
                    Trigrams.append(adder)
                   
                    
        counter = collections.Counter(Trigrams)
        for index in range(0,len(counter.most_common())):
            if(index>=15):
                break
            else:
                sugg.append(counter.most_common()[index][0])
        
        return sugg
    
    else:
        n=len(current)
        for word3,k3 in MainTrigram.items():
                word4=word3.split()
                divisor=word4[0:2]
                divisor=' '.join(divisor)
                if(divisor== previous):
                    adder=word4[2:3]
                    adder=' '.join(adder)
                    #print(adder)
                    Trigrams.append(adder)
        trigrams = collections.Counter(Trigrams)
        #print(bigrams)
        for word2,k2 in trigrams.items():
            for index in range(len(word2)):
                 if(word2[0:n] == current):
                    Trigram_sugg.append(word2)
        counter=collections.Counter(Trigram_sugg)
        for index in range(0,len(counter.most_common())):
            if(index>=15):
                break
            else:
                sugg.append(counter.most_common()[index][0])
        
        return sugg


global All
All=0
def evaluation():
    #print("here")
    global All
    global Total_Keys
    global CountSpaces
    radiovalue=var.get()
    if(radiovalue==1):
        input_usr = user_input.get("1.0",'end-1c')
        input_usr=input_usr.split()
        
        global Total_suggested_Unigram
        for word in input_usr:
            All+=len(word)
        print(All)
        temp=0
        temp=Total_Keys-CountSpaces
#        All=len(input_usr)
        #Total_suggested_Unigram=All-Total_Keys
        if(len(input_usr)==0):
            eva_text.set("Please Type Something!")
        else:
            KS2= ((All-temp)/All)*100
            eva_text.set(KS2)
            All=0
        
    elif(radiovalue==2):
        input_usr = user_input.get("1.0",'end-1c')
        input_usr=input_usr.split()
        
        for word in input_usr:
            All+=len(word)
#        All=len(input_usr)
        print(All)
        temp2=0
        temp2=Total_Keys-CountSpaces
        #Total_suggested_Bigram=All-Total_Keys
        if(len(input_usr)==0):
            eva_text.set("Please Type Something!")
        else:
            KS2= ((All-temp2)/All)*100
            eva_text.set(KS2)
       
    elif(radiovalue==3):
        input_usr = user_input.get("1.0",'end-1c')
        input_usr=input_usr.split()
        
        for word in input_usr:
            All+=len(word)
#        All=len(input_usr)
        print(All)
        temp3=0
        temp3=Total_Keys-CountSpaces
        #Total_suggested_Trigram=All-Total_Keys
        if(len(input_usr)==0):
            eva_text.set("Please Type Something!")
        else:
            KS2= ((All-temp3)/All)*100
            eva_text.set(KS2)
        
    
    
def clear():
        sugg_string.set("")
        user_input.delete(1.0, "end-1c")
        eva_text.set("")
        user_input.insert("end-1c", "")
        listBox.delete(0, tk.END)
        listBox.insert(tk.END, "")
#        btn1_text.set("")
#        btn2_text.set("")
#        btn3_text.set("")
#        btn4_text.set("")
#        btn5_text.set("")
#        eva_text.set("")
        global All
        All=0
        global Total_suggested_Unigram
        Total_suggested_Unigram=0
        global Previous_bigram
        Previous_bigram="<s>"
        global Total_Keys
        Total_Keys=0
        global current_word
        current_word=""
        global Previous_Trigram
        Previous_Trigram="</s> <s>"
        global previousChar
        previousChar=""
        global input_usr2ap
        input_usr2ap=""
        sugg_initial()
      
        global Total_suggested_bigram_Keys
        Total_suggested_Keys=0

        global Total_suggested_Trigram
        Total_suggested_Trigram=0
        
def sugg_initial():
    global Previous_bigram
    global Previous_Trigram
    global current_word
    radiovalue=var.get()
    if(radiovalue==1):
                start=" "
                suggestion=suggestion_of_Unigram(UnigramProb,start)
                if(len(suggestion)==0):
                    listBox.delete(0, tk.END)
                    listBox.insert(tk.END, "No Match")
                   
                else:
                        listBox.delete(0, tk.END)
                        for word in suggestion:
                            listBox.insert(tk.END, word)
                       
    elif(radiovalue==2):
        suggestion=suggestion_of_bigram(BigramProb, current_word,Previous_bigram)
        if(len(suggestion)==0):
                    listBox.delete(0, tk.END)
                    listBox.insert(tk.END, "No Match")
                   
        else:
                        listBox.delete(0, tk.END)
                        for word in suggestion:
                            listBox.insert(tk.END, word)
                        
                        
    
          
    elif(radiovalue==3):
            suggestion=suggestion_of_Trigram(TrigramProb, current_word,Previous_Trigram)
            if(len(suggestion)==0):
                    listBox.delete(0, tk.END)
                    listBox.insert(tk.END, "No Match")
                   
            else:
                        listBox.delete(0, tk.END)
                        for word in suggestion:
                            listBox.insert(tk.END, word)

def close_window(): 
    root.destroy()

label_0 = tk.Label(root, text="Word Prediction Application",width=30,font=("bold", 20))
label_0.place(x=190,y=20)


label_1 = tk.Label(root, text="براہ مہربانی ٹائپ کریں",width=20,font=("bold", 13))
label_1.place(x=500,y=75)



#userInput= tk.StringVar()
user_input = tk.Text(root, bd=15,width=52, height=20)
user_input.bind("<Key>",test)
#user_input.pack()
user_input.place(x=240,y=100)


label_2 = tk.Label(root, text="پیشن گوئی کھڑکی",width=20,font=("bold", 13))
label_2.place(x=670,y=75)

sugg_string= tk.StringVar()
suggestion = tk.Entry(root,textvariable = sugg_string ,bd=15, width=20)
#user_input.pack()

suggestion.place(x=700,y=100,height=350)
#suggestion.pack(ipady=9)



label_3 = tk.Label(root, text="Ngram Model Type",width=20,font=("bold", 15))
label_3.place(x=20,y=100)
var = tk.IntVar()
tk.Radiobutton(root, text="ایک گرام ماڈل",font=("bold", 15),padx = 5, variable=var, value=1, command=sugg_initial).place(x=60,y=130)
tk.Radiobutton(root, text="دو گرام ماڈل",font=("bold", 15),padx = 5, variable=var, value=2, command=sugg_initial).place(x=60,y=160)
tk.Radiobutton(root, text="تین گرام ماڈل",font=("bold", 15),padx = 5, variable=var, value=3, command=sugg_initial).place(x=60,y=190)


tk.Button(root, text='Evaluate',width=20,bg='purple',fg='white', command=evaluation ).place(x=60,y=475)
eva_text = tk.StringVar()
tk.Button(root,textvariable=eva_text, text='Result',width=20,bg='purple',fg='white').place(x=60,y=510)


listBox=tk.Listbox(root, selectmode=tk.SINGLE ,height="20")
#listBox.insert(0,"nadeem")
listBox.place(x=715,y=115)
listBox.bind('<<ListboxSelect>>', test)





tk.Button(root, text='Close',width=20,bg='Brown',fg='white',command=close_window).place(x=300,y=490)
tk.Button(root, text='New Input',width=20,bg='green',fg='white', command=clear).place(x=460,y=490)

root.mainloop()