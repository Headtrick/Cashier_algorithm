# Python3 program to find minimum
# number of denominations
import math as Math
def findMin(money):
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
            index +=1
    
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
    
    #For Testing results
    sum = 0
    for i in range (len(change)):
        sum += change[i]*deno[i] 
    ok = "ok" if int(money)==sum else "NOT OK" 
    print(money," : ", sum ," : ",change, ok)

# Driver Code
if __name__ == '__main__':
    #TEST
    #A Hundred TL
    #Two Hundred KRŞ
    tl_list_one= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,22, 23, 24, 25,
    26, 27, 28, 29, 30, 31, 32, 33,34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,47, 48, 49, 50, 51, 52,
     53, 54, 55, 56, 57, 58, 59, 60,61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,75, 76, 77, 78, 79,
      80, 81, 82, 83, 84, 85, 86, 87, 88, 89,90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100]
    tl_list_two= [100,101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,113, 114, 115, 116,
     117, 118, 119,120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135,136,
      137,138, 139, 140, 141, 142, 143, 144, 145, 146, 147,148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 
      158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177,
       178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]
    
    krs_list= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,22, 23, 24, 25,26, 27, 28, 29, 30, 
    31, 32, 33,34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,61, 62,
     63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,90, 91, 92, 93, 94,
      95, 96, 97, 98, 99,100]
    
    #Testing for 200 cases
   
   

        #findMin(input_tl+input_krs)
    findMin(str(985342523523534) +str(22) )

# This code is contributed by
# Ertuğrul Gürler
