
def leap_year(a):
    if (a%4==0 and (a%100!=0 or a%400==0)):
        print ("liap year")
    else:
        print("not a liap year")

leap_year(2027)


def anagrams(a,b):
    
    
    if sorted(a)==  sorted(b):
        print ("it is a anagram")
    else: 
        print("not a anagrasm")

anagrams("listen","silent")


def lcm(a,b):
    lcm=max(a,b)
    while True:
        if lcm%a==0 and lcm%b==0:
            print(lcm,"is the list multipal")
            break
        lcm+=1
    return lcm
lcm(2,3)
                                                                                                                