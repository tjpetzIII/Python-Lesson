# Thomas Petz
# Selection Sort 
# Selction sort runs on O(n^2)



def selection_sort(array) :
    #First for loop
    for i in range (0, len(array) -1):
        print(array)
        print()
        minIndex = i
        for j in range (i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j

        #swapping num at position i with the minimum value of the unsorted array       
        temp = array[i]
        array[i] = array[minIndex]
        array[minIndex] = temp

#define array to be sorted
array = [5, 4, 7, 8, 2, 9, 3]

#call selection sort on the array
selection_sort(array)

#Print the result of the sort
print("Sorting complete")
print(array)



