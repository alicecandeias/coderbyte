'''Have the function ArrayChallenge(arr) take the array of numbers stored in arr and return the index at which the numbers stop increasing and begin decreasing or stop decreasing and begin increasing.
For example: if arr is [1, 2, 4, 6, 4, 3, 1] then your program should return 3 because 6 is the last point in the array where the numbers were increasing and the next number begins a decreasing sequence.
The array will contain at least 3 numbers and it may contains only a single sequence, increasing or decreasing. If there is only a single sequence in the array, then your program should return -1.
Indexing should begin with 0.'''

def ArrayChallenge(arr):

  #if min and max are at index 0 and len(arr), return -1 bc indicates only 1 sequence increasing or decreasing 

  if arr.index(max(arr))==0 and arr.index(min(arr))+1==len(arr) or arr.index(max(arr))+1==len(arr) and arr.index(min(arr))==0:
    return -1
  
  # other cases
  
  else:
    
    flag = 0

    for i in range(len(arr)-1):
      if arr[i] < arr[i+1]:
        if flag==0:
          flag = 1
        elif flag == -1:
          return i

      elif arr[i]>arr[i+1]:
        if flag == 0:
          flag = -1
        elif flag == 1:
          return i
      
     
  return arr

# keep this function call here 
print(ArrayChallenge(input()))

---------------------------------------------------------------------------


#I've made a second one

def ArrayChallenge(arr):

    flag = 0

    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            if flag==0:
                flag = 1
        elif flag == -1:
            return i
        
        elif arr[i]>arr[i+1]:
            if flag == 0:
                flag = -1
        elif flag == 1:
            return i

    return -1
        

# keep this function call here 
print(ArrayChallenge(input()))
