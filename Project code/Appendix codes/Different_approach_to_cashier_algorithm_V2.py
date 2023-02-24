import math as Math
def findMin(money,limit):
    # All denominations of Turkish Currency
    deno = [20000, 10000, 5000, 2000, 1000,
            500, 100, 50, 25, 10, 5, 1]
    change = [0,0,0,0,0,0,0,0,0,0,0,0] 
    #Take first 4 digits into an array
    key = len(money)
    digits = []
    for i in range (key-1,key-5,-1):
        index = 0
        if i<0:
            digits.insert(0,0) #In case of 1 digit of krs is entered
        else:
            digits.insert(index,int(money[i]))
    #Take rest of them and convert to int
    if key>4:
        money_without_four_digits = int(money[:-4])
        #For number of 200 TL update the change list
        number_of_twohundred = Math.floor(money_without_four_digits/2)
        number_of_onehundred = money_without_four_digits%2
        change[0] += number_of_twohundred
        change[1] += number_of_onehundred 
    #For the tens digit
    tens_digit = digits[0]
    if tens_digit>=5:
        change[2] += 1 #Number of fifties can only be just one
        tens_digit -= 5 
    if tens_digit >=2:
        number_of_twenties=Math.floor(tens_digit/2)
        change[3] += number_of_twenties
        tens_digit -=2*number_of_twenties
    change[4] += tens_digit
    #For the ones digit
    ones_digit = digits[1]
    if ones_digit>=5 :
        change[5] += 1
        ones_digit-=5
    change[6] += ones_digit
    #For the first and second digit of KRŞ
    ten_krs_digit = digits[2]
    one_krs_digit = digits[3]
    if ten_krs_digit >=5:
        change[7] += 1
        ten_krs_digit -=5
    if (ten_krs_digit >=2) and (one_krs_digit >=5):
        change[8] += 1
        ten_krs_digit -=2
        one_krs_digit-=5
    elif (ten_krs_digit >2) and (one_krs_digit <5):
        change[8] +=1
        ten_krs_digit -=3
        one_krs_digit +=5
    change[9] += ten_krs_digit
    if one_krs_digit >=5:
        change[10] += 1
        one_krs_digit -=5
    change[11] += one_krs_digit

    # CHANGING THE MONEY THAT WILL BE GIVEN ACCORDING TO BOUNDRIES
    try:
        for i in range(11):
            if limit[i]<change[i]:
                diff = change[i]-limit[i]
                if (i==2) or (i==8):
                    change[i+1]+=diff*2
                    change[i+2]+=diff
                    change[i]-=diff                
                elif (i==5) or (i==10):
                    change[i+1]+=diff*5
                    change[i]-=diff
                else:
                    change[i+1]+=diff*2
                    change[i]-=diff
    except:
        print("There is not enough money in the safe")
        exit()
    
    #For Testing results
    sum = 0
    for i in range (12):
        sum += change[i]*deno[i] 
    ok = "ok" if int(money)==sum else "NOT OK"
    print(limit)
    print(change," : ",sum,":",ok)  

# Driver Code
if __name__ == '__main__':    
    #Take limits from the user O(M) WHERE M IS AMOUNT OF LIMIT
    limits=[]
    str = ["200 TL : ", "100 TL : ", "50 TL : ", "20 TL : ", "10 TL : ",
            "5 TL : ", "1 TL : ", "50 KRŞ : ", "25 KRŞ : ", "10 KRŞ : ", "5 KRŞ : ", "1 KRŞ : "]
    print("Enter limits : ")
    for i in range (12):
        print(str[i])
        limits.append(int(input()))
    # ENTER MONEY
    print("Enter TL: ")
    tl = input()
    print("Enter KRS (Only two digits): ")
    krs = input()
    if len(krs)==1:
        krs = "0"+krs
    if len(krs)>2:
        print("Enter just two digits : ")
        krs = input()
        findMin(tl+krs,limits)
    findMin(tl+krs,limits)

    

# This code is contributed by
# Ertuğrul Gürler
