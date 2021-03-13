import math
import sympy
import time
import random
t0=time.time()
p=int(input("Enter prime p: "))
q=int(input("Enter prime q: "))
n=p*q;d1=34;key=7
pi=(p-1)*(q-1)
for i in range(2,pi):
    if(sympy.isprime(i)):
        if(i!=p and i!=q):
            if(math.gcd(i,pi)==1):
                e=i
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
d=modInverse(e,pi);x1=[];y1=[]
r=int(input("Enter a random number :"))
count=0
for i in range(1,500):
    for j in range(1,500):
        if(pow(i,4)*j-r*pow(j,3)==1):
            count+=1
            x1.append(i);y1.append(j)
if(count==0):
    print("no answers select another random number")
print("possible values of x and y are :",x1,y1)
x=x1[0];y=y1[0]
print("x y :",x,y)
if(pow(x,4)-r*pow(y,3)==1):
    print("TESTCASE-1: Testcase for x and y is successful")
else:
    print("TESTCASE-1: Testcase for x and y is not successful")
al1=((x+e)*(x+e)*(x+e)*(x+e)*(y+pi))%pi+(-(y+pi)*(y+pi)*(y+pi)*r)%pi
ver=(al1-(e*e*e*e*y)%pi-(4*x*y*e*e*e)%pi-(4*x*x*x*e*y)%pi-(6*x*x*e*e*y)%pi)%pi
print("e is ",e," pi(n) is ",pi," verification alpha is",ver);print("")
if(ver==1):
    print("TESTCASE-2: Testcase for alpha is successful")
else:
    print("TESTCASE-2: Testcase for alpha is unsuccessful")
print("Private Keys are :- e:",e," N:",n)
print("Public keys are :-(e^3y+4x^3y+6x^2ey+4xye*2)%pi(n) :",((e*e*e*y)+(4*x*x*x*y)+(6*x*x*e*y)+(4*x*y*e*e))%pi," alpha:",al1," N:",n);print("")
print("Encryption :")
te1=time.time()
f=open("Review3\\1kb\\indian.txt", "r",encoding="mbcs")
if(f.mode=='r'):
    m =f.read()
f.close()

#print(m)
l=list(m.split(" "))
l1=[]
for i in l:
    l2=[]
    for j in i:
        l2.append(ord(j))
    l1.append(l2)



l3=[];l4=[]
for i in l1:
    l3a=[];l4a=[]
    for j in i:
        ct1=pow(j,al1)%n
        ct2=pow(j,((e*e*e*y)+(4*x*x*x*y)+(6*x*x*e*y)+(4*x*y*e*e))%pi)%n
        l3a.append(ct1)
        l4a.append(ct2)
    l3.append(l3a)
    l4.append(l4a)

s1='';s2=''
for i in range(0,len(l3)):
    for j in range(0,len(l3[i])):
        s1+=chr(l3[i][j])
        s2+=chr(l4[i][j])
    s1+=' ';s2+=' '
print("Encrypted Strings:")
f= open("Review3\\1kb\\Encrypted_string1_indian 1 kb.txt","w+", encoding='utf-8')

f.write(s1)
f.close()
print("Encrypted data-1 file written successsfully")
s11='';s12='';s22='';s21=''
for i in s1:
    if(i==' '):
        s11+=s12+' '
        s22+=s21+' '
        
        s12='';s21=''
    else:
        v=ord(i)
        c=v-d1
        if(v-d1>0):
            s12+=chr(c^key)
            s21+=chr(d1^key)
if(len(s12)>0 or len(s21)>0):
    s11+=s12
    s22+=s21

f= open("Review3\\1kb\\cloud-A Encrypted_string1_indian 1kb.txt","w+", encoding='utf-8')
f.write(s11)
f.close()

f= open("Review3\\1kb\\cloud-B Encrypted_string1_indian 1kb.txt","w+", encoding='utf-8')
f.write(s22)
f.close()

s11r='';s22r=''
for i in range(0,len(s11)):
    if(s11[i]!=' '):
        s11r+=chr(ord(s11[i])^key)
        s22r+=chr(ord(s22[i])^key)
    else:
        s11r+=' ';s22r+=' '
"""
f= open("Review3\\1kb\\cloud-A_retrieval Encrypted_string1_indian 1kb.txt","w+", encoding='utf-8')
f.write(s11r)
f.close()

f= open("Review3\\1kb\\cloud-B_retrieval Encrypted_string1_indian 1kb.txt","w+", encoding='utf-8')
f.write(s22r)
f.close()
"""
sf=''
for i in range(0,len(s11r)):
    if(s11r[i]!=' '):
        sf+=chr(ord(s11r[i])+ord(s22r[i]))
    else:
        sf+=' '
f= open("Review3\\1kb\\cloud_retrieval-final Encrypted_string1_indian 1kb.txt","w+", encoding='utf-8')
f.write(sf)
f.close()

    



f= open("Review3\\1kb\\Encrypted_string2_indian 1 kb.txt","w+", encoding='utf-8')
f.write("Encrypted Information:")
f.write(s2)
f.close()
print("Encrypted data-2 file written successsfully")
te2=time.time()
print("Time taken for encryption :",round(te2-te1,3))

s11='';s12='';s22='';s21=''
for i in s2:
    if(i==' '):
        s11+=s12+' '
        s22+=s21+' '
        
        s12='';s21=''
    else:
        v=ord(i)
        c=v-d1
        if(v-d1>0):
            s12+=chr(c^key)
            s21+=chr(d1^key)
if(len(s12)>0 or len(s21)>0):
    s11+=s12
    s22+=s21    

f= open("Review3\\1kb\\cloud-A Encrypted_string2_indian 1kb.txt","w+", encoding='utf-8')
f.write(s11)
f.close()

f= open("Review3\\1kb\\cloud-B Encrypted_string2_indian 1kb.txt","w+", encoding='utf-8')
f.write(s22)
f.close()

s11r='';s22r=''
for i in range(0,len(s11)):
    if(s11[i]!=' '):
        s11r+=chr(ord(s11[i])^key)
        s22r+=chr(ord(s22[i])^key)
    else:
        s11r+=' ';s22r+=' '
"""
f= open("Review3\\1kb\\cloud-A_retrieval Encrypted_string1_indian 1kb.txt","w+", encoding='utf-8')
f.write(s11r)
f.close()

f= open("Review3\\1kb\\cloud-B_retrieval Encrypted_string1_indian 1kb.txt","w+", encoding='utf-8')
f.write(s22r)
f.close()
"""
sf1=''
for i in range(0,len(s11r)):
    if(s11r[i]!=' '):
        sf1+=chr(ord(s11r[i])+ord(s22r[i]))
    else:
        sf1+=' '
f= open("Review3\\1kb\\cloud-_retrieval-final Encrypted_string2_indian 1kb.txt","w+", encoding='utf-8')
f.write(sf1)
f.close()





print("Decryption :");de=''
td1=time.time()
for i in range(0,len(s1)):
    if(s1[i]!=' '):
        #print((ord(s1[i])*pow(ord(s2[i]),(-e)%pi))%n,end="  ")
        de+=chr(int(ord(s1[i])*pow(ord(s2[i]),(-e)%pi))%n)
    else:
        de+=' ';
f= open("Review3\\1kb\\Decrypted informantion_1kb.txt","w+", encoding='utf-8')
f.write("Decrypted Information:")
f.write(de)
f.close()
print("Decrypted data file written successsfully")
td2=time.time()
print("Time taken for decryption :",round(td2-td1,3))
print("Technique successful")

