#Program to input a number upto 5 digits and print it in words
ones=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
n=int(input("Enter number less than 99999 "))
if n>99999:
    print("I Can't solve... You've entered more than 5 digits")
else:
    d=[0,0,0,0,0]
    i=0
    while n>0:
        d[i]=n%10
        i+=1
        n=n//10
    num=""                                                                              #56321
    if d[4]!=0:                                                                         #[1,2,3,6,5]
        if(d[4]==1):                                                                    #[0,1,2,3,4]
            num+=tens[d[3]]+ " Thousand "                                   # 3000     three thousand
        else:
            num+=nty[d[4]]+" "+ones[d[3]]+ " Thousand "
    elif d[3]!=0:
        num+=ones[d[3]]+ " Thousand "
    if d[2]!=0:
        num+=ones[d[2]]+" Hundred "
    if d[1] != 0:
        if (d[1] == 1):
            num+=tens[d[0]]
        else:
            num+=nty[d[1]] + " " + ones[d[0]]                            #23   twenty three       nty number
    elif d[0]!=0:
        num+=ones[d[0]]
    print(num)