from __future__ import print_function
from array import *
from collections import Counter
import numpy as np
import sys
import operator
import time
from datetime import timedelta
import math
from collections import deque
import qrcode


start_time = time.perf_counter()

print('Hie')




""" print("to upper")
string = input()

string = string.upper()
print(string)
print("to lower")
string2 = input()
string2 = string2.lower()
print(string2)




 num  =int(input())
arr = int([])
for i in range(num):
    arr = input()

for i in range(arr):
    print(i) 


#test = int(input())

string1 = 'Ajay'
string2 = 'sinha'

print(string1+string2)

print((string1+string2)*2)

print(string1[:3])

my_dict = {'name':'ajay', 'brother ':'anupam', 'mom ':'mom', 'dda':'dad',4:'another'}
print(my_dict['brother '])

'''for  loop in range(1):
    print('root loop',loop)
    for loop2 in range(1) :
        print('i am loop 2',loop2)
        for loop3 in range(1):
            print('i am in lop 3',loop3)
            for loop4 in range(2):
                print('i amm in looop 4',loop4)'''

'''def add(a,b):
    #num1 = int(input())
    #num2 = int(input())
    
    sum = a+ b
    return sum '''



#print(add(num1,num2))  
"""   #comment end here

'''def calc():
 num=0
num = int(input())
for i in range(1,num):
        if(i%2==1):
            for j in range(i**2):
             str(i)
             print(i,end='')


for i in range(1,num):
                 if (i % 2 == 0):
                     for j in range(i**2-1):
                         str(i)
                         print(i, end='')


calc()'''

#hackerEarth Problems

'''mul=1
t = int(input())
numbers = input().split(' ')
for i in range(t):
    k=int(numbers[i])
    mul=(mul*k)%1000000007
print(mul)'''


#hackerEarth Problems

'''t = int(input())
for i in range(t):
   str1 ={str(input())}
   str2 = str(input())

if(Counter(str1)==Counter(str2)):
     print('yes')
else:
    print('false')'''

#sample
'''faliure = 100
dream = 01
while(faliure<dream):
    faliure = faliure+1
    if(faliure==dream):
        print("Success")
    else:
        print("fail again",faliure,"times")


print("SO Learn how to fail")'''



#hackerEarth practice revesing the array
'''size = int(input())
arr = []
for loop in range(size):
    arraySize = int(input())
    arr.append(arraySize)

for i in reversed(arr):
 print(i)'''

#finding the min element in list
''''sequence = []
minList = []
lenghtOfseq =  int(input())
for loop in range(lenghtOfseq):
    value = int(input())
    sequence.append(value)
minList.append(min(sequence))

for loop in min(sequence):
    print(minList)'''




'''string1 = input()             #company challange not solved 
                                # (i)rebel (ii)reebel show how many and wich letter is required to make it like (ii)  if not possible print "not possible"
string2 = input()
length1 = sum(map(ord,string1))
length2 = sum(map(ord,string2))
diff = length2-length1
charecter = chr(diff)
  
print(charecter)'''



'''a = np.arange(15).reshape(3, 5)       #numpy Example
print(a)'''

#codeChef Problems  fancy ,Regular Fancy  #not- solved :(

'''testCase = int(input())
for loop in range(testCase):
    string = input()
      
if(string.find('not')!= -1):
    print('fancy')
else:
    print('regularfancy')'''




'''test=int(input())   #anagram problem hacker earth
for i in range(test):
    a=list(input())
    b=list(input())
k=0
if len(a)<=len(b) :
    for loop in range(len(a)):
        if a[loop] in b:
            k=k+1
            value=b.index(a[y])
            b[value]='0'
else:
 for loop in range(len(b)):
                if b[loop] in a:
                    k=k+1
                    value=a.index(b[y])
                    a[value]='0'

print((len(a)-k)+(len(b)-k))'''

#plaindrome problem hacker earth
'''string = input()
string.lower()
if(len(string)<=100):
    if(string == string[::-1]):
     print('yes')
else:
    print('no')'''  #solved


'''while True:    #hackerrank practice

        n = int(input())
        if n <=1 or n<=10:
            fact=0
            for loop in range(n):
             fact = n * loop
            break
print(fact)'''   #solved



'''from bs4 import BeautifulSoup
import requests
url = '#please specify site url here'
resp = requests.get(url)
soup = BeautifulSoup(resp.text)
tr = soup.findChildren('tr')
tr = iter(tr)
next(tr)
for movie in tr:
    title = movie.find('td',{'class':'titleColumn'}).find('a').contents[0]
    print(title)'''


#welcome Monk Array and string Q1

'''sum  = []
test_case = int(input())
arrayvaluesA = list(map(int, input().split(None,test_case)[:test_case]))  *not comftable with taste case 
arrvaluesB = list(map(int, input().split(None,test_case)[:test_case]))
sum = np.add(arrayvaluesA,arrvaluesB)
print(sum)''' #soved   #we can also add it without using numpy


'''#Default argument Values More on functions
def ask_ok(prompt , retries = 4 , remainder = 'please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y','yes','ya','haha'):
            return True
        if ok in ('n','no','naaa','nopes','nahi'):
            return False
        retries = retries-1
        if retries < 0:
            raise ValueError('invalid user response')
        print(remainder)

ask_ok('do you want really to quit',1,'again want to try')'''

'''def calculate(sum):
    a = 10
    b = 20
    sum = a+b
    return sum    # returning the function

storeFun  = calculate(sum)
print(storeFun)''' # function can also be stored in a variable so it can be called

'''def cheeseshop(kind , *arguments, **keywords):    #functions from docs
    print("--do have any ", kind, "?")
    print("--I am sorry , we're all out of",kind)
    for arg in arguments:
        print(arg)
    print("-" * 10)
    for kw in keywords:
        print(kw,":",keywords[kw])



cheeseshop("stuff","its a really very,very Very runny,sir",
           shopkeeper = "Micheal palin",
           client = "micheal palin",
           sketch = "cheese shop Sketch")'''


'''n = int(input())
fact = 1
for loop in range(1,n+1):
    fact = fact*loop

print(fact)'''

#prime numberes     ''' please rechek it'''
'''num = int(input())
for loop in range(1,10+1):
    if loop > 1 :
        for n in range(2,loop):
            if(loop%n == 0):
                break
            else:
                print(loop)'''  #solved

#hackeEarth Memorise me Problem
'''no_of_shown_integers = int(input())
List_A = [int(no_of_shown_integers) for no_of_shown_integers in input().split()]
count = Counter(List_A)
no_of_ints = int(input())
for i in range(no_of_ints):
    query = int(input())
    print(count[query]if count[query]>0 else "not present")'''    # *Solved

#HackerEarth welcome monk                 Q.adding two list
'''size = int(input())
List_A = [int(size) for size in input().split()]
List_B = [int(size) for size in input().split()]


List_C = [List_A[i]+List_B[i] for i in range(len(List_A)) ]

print(' '.join(map(str,List_C)))'''      ##solved

#haackerEarth Problems Lucky unlucky

'''test_case = int(input())
for loop in range(test_case):
    size = int(input())
    arr = [int(size) for size in input().split()]
    m = min(arr)
    cnt = arr.count(m)
    if(cnt%2==1):
        print('Lucky')
    else:
        print('Unlucky')'''    ## solved


# Book Of Potion making  #tags : - easy
'''legal = 0
isbn = input()
isbn =[int(i) for i in isbn]
for loop in range(len(isbn)):
    legal += ((loop+1)*isbn[loop])

if(legal%11==0):
    print("Legal ISBN")
else:
    print("illegal ISBN")'''    ##solved


# Magical word             #tags : easy-medium

'''test_case = int(input())
for loop in range(test_case):
    str_size = int(input())
    arr = [(str_size) for str_size in input()]
new_arr = []
for values in arr:
    ascii = ord(values)
    new_arr.append(ascii)
for loop in range(len(new_arr)):
    for i in range(loop):
        if(i%loop==0):
            break
        else:
            print(loop)

#print(' '.join(map(str,new_arr)))'''    #not-solved  Please solve it later

#juneeasy challange hackerEarth
'''length = int(input())
num_of_pics = int(input())
for loop in range(num_of_pics):
    width,height = [int(width) for width in input().split()]
    dimension = (width * height)
    if (width < length or height< length):
        print("UPLOAD ANOTHER")
    elif(dimension == length**2 or dimension == width**2):
     print("Accepted")
    else:
     print("CROP IT")'''      #  Solved


# motu patlu BRickGame hackerEarth

'''bricks = int(input())
for loop in range(bricks,-1,-1):
    patlu = loop
    motu = (patlu * 2)
    count = motu + patlu
    if(count == motu):
        print('Motu')
    elif(count == patlu):
        print('Paltu') ''' #correction is required as not all test cases are passing


# Two Strings ** use hash concept only **
''' test_case = int(input())
val = 0
val2 = 0
for loop in range(test_case):
    str1,str2 =(str(str1) for str1 in input().split())
    for i in str1:
        val += hash(i)
    for j in str2:
        val2 +=hash(j)
    if(val == val2):
        print('YES')
    else:
        print('NO') ''' #Partially solved sample test case 5 not paasing


#   Ali helping people
'''s = input()
vowels = ['A','E','I','O','U','Y']
if (int(s[0])+int(s[1]))%2==0 and (int(s[3])+int(s[4]))%2==0 and (int(s[4])+int(s[5]))%2==0 and (int(s[7])+int(s[8]))%2==0:
    if s[2] not in vowels :
        print('valid')
    else:
        print('invalid')
else:
    print("invalid")''' #solved


# Pepper and Contigious Even Subarray      **  asked in : Tata Health java Hiring
'''test_case = int(input())
for loop in range(test_case):
    count = 0
    max = 0
    size = int(input())
    arr = [int(size) for size in input().split()]
    for i in range(len(arr)):
        if(arr[i]%2==0):
            count +=1
        else:
            count = 0
        if(count > max) :
            max = count
    print(max if max > 0 else '-1')'''

'''st = input()   #hackerEarth Toggle String
ct = ''
i = 0
if len(st)>100 :
    sys.exit()
else:
 for s in st:
  if s.islower() is True:
      c = s.upper()
      ct = ct[i:] + c + ct[:i]
  if s.isupper() is True:
       c = s.lower()
       ct = ct[i:] + c + ct[:i]
print(ct)''' #solved **


#Helping Jarvis
'''test_case = int(input())
for loop in range(test_case):
    list_A = list(map(int, input().split()))
if sorted(list_A) == list_A:
    print('NO')
else:
    print('yes')''' #not solved


# Duration tag(s) : easy

'''wrk = int(input())
for loop in range(wrk):
    dur = [int(i) for i in input().split()]
    wrk_dn = (int(dur[2])*60 + int(dur[3])) - int((dur[0])*60+int(dur[1]))
    secs = (wrk_dn*60)
    hours = secs // 3600
    minutes = secs // 60 - hours * 60
    length = "%d %02d" % (hours, minutes)
    print(length) ''' # all test case are not passing please try again

# problems from codeChef tags- beg q - Total Expense

'''test_case = int(input())
for loop in range(test_case):
    quant , price = [int(x) for x in input().split()]
    expense = (quant * price)
    if(quant>1000):
        disc = (10//100)*expense
        act_prc = expense - disc
        print(act_prc)
    else:
        print(expense) ''' #problem solved but cant run in CodeChef


'''def main():

 # Write code here
 str1 = "Hello TechGig"
 str2 = input()
 print(str1)
 print(str2)


main()'''

'''testcs = int(input())
if(testcs<=10):
    for loop in range(testcs):
        start , end = [int(x) for x in input().split()]
        for num in range(start, end+1):
            if all(num%i!=0 for i in range(2,int(math.sqrt((num))+1))):
                print(num)'''

# PRoblems on stack  tag: - frustated coders  # kiiling the coders with less skill   :(

'''no_of_coders = int(input())   #input  for no of coders
skills = [no_of_coders  for no_of_coders in input().split()]  #input for their skills
for i in range(no_of_coders):
    if(skills[0] < skills[1]):
     print(skills[1]) '''  # try solving it later



# monk teaches PlainDrome

'''def reverse():
    test_case = int(input())
    for loop in range(test_case):
        str = input()
        rev = str[::-1]
        if(str == rev ):
         print("YES")
        else:
         print("NO")


reverse()'''  #solved


# max tweet count

'''count  = 0
user = []
test_case  = int(input())
for loop in range(test_case):
    no_of_tweets = int(input())
    for loop2 in range(no_of_tweets):
        tweets = str(input())
        user.append(tweets)
    same_names  = [names.split()[0] for names in user]
    times = Counter(same_names)
    dict_values = times.values()
    val = max(times.values())
    result = [(name, twt_cnt) for name, twt_cnt in sorted(times.items()) if twt_cnt == val]
    for name, twt_cnt in result:
        print(name, '', twt_cnt)'''   ##partially solved


## shift string in left order
'''shifted = []
alphabets = str(input())
k_position  = int(input())
#size = len(alphabets)
for loop in range(len(alphabets)):
    idx  = (loop + k_position)% len(alphabets)
    shifted[idx:idx]  = alphabets[loop]

print(shifted)'''

## Sort the subarray in decending order   ##basic
'''sorted_s = []
test_case = int(input())
for loop in range(test_case):
    alphabets , N  , M = (str(alphabets) for alphabets in input().split())
    left_index  = int(N)
    right_index  = int(M)
    print(alphabets[:left_index]+"".join(sorted(alphabets[left_index:right_index+1],reverse=True))+ alphabets[right_index+1:])'''




## harry and doughnuts  SPOJ

'''test_case = int(input())

for loop in range(test_case):
    c, k  , w = [int(c) for c in input().split()]
    temp_weight = c*w
    if(temp_weight<=k):
        print("yes")
    else:
        print("no")'''    ##solved

## Short Name  for ex :sample I/O   Ajay Kumar Sinha      A. K. Sinha

'''names = str(input())
for loop in range(len(names)):
    short  = names[:-3]    ##shorting the names to only one letter

print(short)'''   ##please solve it later


## hourGlass hackerRank
'''def hourglass_Sum():
    mat = []
    for _ in range(6):
        mat.append(list(map(int,input().split())))
   # for row in range(len(mat)):                ## for printing the matrix
   #    for col in range(len(mat)):             ## row and column wise
   #    print(mat[row][col],end =" ")
   #   print()
    maxim_total = -1073741824
    num_rows = len(mat)
    num_cols =(len(mat[0]))
    for row in range(num_rows-2):
        for col in range(num_cols-2):
            maxim = (mat[row][col]+mat[row][col+1]+mat[row][col+2])+(mat[row+1][col+1])+(mat[row+2][col]+mat[row+2][col+1]+mat[row+2][col+2])
            if(maxim_total<maxim):
                maxim_total = maxim

    print(maxim_total)
hourglass_Sum() ''' ## solved althoug it was basic but you need to know the logic behind adding it

## array Left_rotation

'''size , rotation = [int(size)for size in input().split()]
arr= [int(size) for size in input().split()]
n = len(arr)
#for loop in range(len(arr)):
    #idx = (loop+rotation)%len(arr)
#result = arr[-n + rotation:] + arr[:rotation]
result = arr[rotation:] + arr[rotation:]

print(result)'''


'''lst = [1, 2, 3, 4, 5]
k = 3
n = 5
result = lst[-n + k:] + lst[:k]
print(result)'''

#array right rotation
#lst = [1,2,3,4,5]

'''test_case = int(input())
for loop in range(test_case):
    size , rotation = [int(size) for size in input().split()]
    #neg -= rotation
    arr = [int(size) for size in input().split()]
    result = deque(arr)
    result.rotate(rotation)
    print(*result,sep=' ')''' # try to solve uwithout using deque


## Play with indexes in array
'''transformed = []
print('enter the size of list ')
size = int(input())
play_with_list = [int(size) for size in input().split()]
li , ri = [int(li) for li in input().split()]
play_with_list[li:ri]
#traformed[:] = play_with_list[:ri]
print(play_with_list[ri])

#print(play_with_list)'''



## Infinite arrays #capillary hiring challange
'''results = 0
concatnated_arr = []
test_case = int(input())
for loop in range(test_case):
    arr_size = int(input())
    arrA = [arr_size for arr_size in input().split()]
    len_arrA = len(arrA)
    queries = int(input())
    for loop in range(queries):
        l_idx = int(input())
    #for loop in range(queries):
        r_idx =  int(input())

        for i in arrA:
            concatnated_arr.extend(arrA*10)
        concatnated_arr = list(map(int,concatnated_arr ))
        for i in range(l_idx-1,r_idx):
            results +=concatnated_arr[i]

            results = sum(concatnated_arr[l_idx-1:r_idx])

print(concatnated_arr)
print(results) ''' #try to form infinite subarray + l_idx and r_indx should be organized n a better way


## long atm queue
                                                                                            # / \ #
# queue standing in increasing order |_1_|_2_|_3_|_4_|_7_|_8_|_9_|_4_|_7_|_8_|_9_|_1_|_2_| |_atm_|
'''count = 1
n = int(input())
queue_ht = [int(n) for n in input().split()]
for i in range(len(queue_ht)):
    try :
        if (queue_ht[i]<queue_ht[i+1]):
            #(queue_ht[i]-queue_ht[i+1]>0): ## the logic is in this line
            #print(queue_ht[i+1])
            # queue_ht[i] = queue_ht[i]
            count +=1
        #else:
            #print('no')
    except:
        #print('there is an error')
        pass

print(count)'''           ##solved

## helping Jarvis
'''
test_case = int(input())
coach_seq =[]
temp = []
sum = 0
for iterate in range(test_case):
    coach_seq = [int(coach_seq) for coach_seq in input().split()]
    coach_seq.sort()
    for i in range(len(coach_seq)):
        if(coach_seq[i] is not coach_seq[i-1]+1):
            print("no")
        else:
            print("yes")


print(temp)
'''


## test case 1,2, 3, 7,8,9 ,10  are unclear... Please try to read question statement again and resolve it later

#compress the string
'''tc = int(input())
strings = []
new_str = []
char = 'abcde'
replace = 'a3e'
try:
    for iterarte in range(tc):
        size = int(input())
        strings = [size for size in input()]
        for loop in range(len(strings)):
            strings[0] = strings[0].upper()
        #for i in range(len(strings)):
            if(strings[0+1] == char[0]):
                strings[0+1] = replace

except:
    pass


print(strings)'''                 #not solved :(



#not in range
'''boxes = []
add =0
for loop in range(1000000):
    boxes.append(loop)
test_case = int(input())
for _ in range(test_case):
    L , R  = [int(L) for L in input().split()]
    for loop in range(L,R+1):
        add +=boxes[loop]
    
print(boxes)
print(add)'''

'''for loop in range(15):
    if loop%3==0:
        print("buzz")
    else:
     print("fizz")
'''

#simple fibonacci :)
'''a=1
b=0
while(a<40):
    print(a)
    a,b = b, a+b
'''

#hackerRAnk match the socks


num = int(input())
lst = [int(num) for num in input().split()]

count = 0
for loop in lst:
    if(loop == lst[loop]):
        count = count+1
print(count)









































































































































































































































































































































































































































































































































































print('secs ---> %s'%(time.perf_counter()- start_time))