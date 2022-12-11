import re
def val_num(num):
    if(re.search(r'^\+1[-| ]?\d{3}[-|.]?\d{3}[-|.]?\d{4}$|^\+?1?[-]?\d{3}[-|.| ]?\d{3}[-|.| ]?\d{4}$',num)):  
        print("Valid Number")  
          
    else:  
        print("Invalid Number")
val_num("(212)-456-7890")
val_num("(212)456-7890")
val_num("+12124567890")
val_num("2124567890")
val_num("212-456-7890")
val_num("212.456.7890")
val_num("212 456 7890")
val_num("+1 212.456.7890")
val_num("+212-456-7890")
val_num("1-212-456-7890")
