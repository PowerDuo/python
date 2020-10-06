#program to sort an array (via bubblesort method)

def bubblesort(array):

    n = len(array)

    #traverse through all of the array elements
    for i in range(0,n-1):
        
        #traverser the array from 0 to n-i-1
        for j in range(0,n-i-1):
            
            #checks if the element found in greater than the element on its right
            if (array[j] > array[j+1]):
                
                #swaps the greater element with the smaller one
                array[j] , array[j+1] = array[j+1] , array[j]
                
    #outputs the array
    print(array)


m = int(input('Enter the number of elements in the array '))

mylist = []

for i in range(0,m):
    num = int(input('Enter element: '))
    mylist.append(num)

bubblesort(mylist)
