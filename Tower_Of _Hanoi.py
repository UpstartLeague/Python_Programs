#Taking input from user
n=int(input("Enter the number of disk(s):-"))

# Creating a recursive function  
def towerofhanoi(n,rod1,rod2,rod3):
    if(n== 1):
        print("Move disk 1 from rod {} to rod {}.".format(rod1,rod3))  
        return  
    
    # function call itself  
    towerofhanoi(n-1,rod1,rod3,rod2)  
    print('Move disk {} from rod {} to rod {}.'.format(n,rod1,rod3))  
    towerofhanoi(n-1,rod2,rod1,rod3) 

# Calling the function    
towerofhanoi(n,'A','B','C')