
def star(arr):
 
    for i in range(len(arr)):
        x = ""
        for l in range(arr[i],0,-1):
            x += "*"   
        print x
star([4,6,1,3,5,7,25])
    
def star_two(arr):
    
    for element in arr: 
        if type(element) == int:
            x = ""
            for i in range(element):
                x += "*"   
            print x
        if type(element) == str:
            e = ""
            for i in range(len(element)):
                e += element[0]
            print e

star_two([4,"tom",1,"micheal",5,7,"jimmy smith"])
    