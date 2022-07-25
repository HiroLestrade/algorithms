def findNth(arr, len, nth):
  leftPivot = 0
  rightPivot = len - 1
  while(leftPivot < rightPivot):
      found = arr[nth]
      leftIndex = leftPivot
      rightIndex = rightPivot
      
      #While pivots don't cross
      while(leftIndex <= rightIndex):
          while arr[leftIndex] < found: leftIndex+=1    #Find a left element in the right
          while arr[rightIndex] > found: rightIndex-=1  #Find a right element in the left
          if(leftIndex <= rightIndex):
              #Swap
              temp = arr[leftIndex]
              arr[leftIndex] = arr[rightIndex]
              arr[rightIndex] = temp
              #Shift indexes
              leftIndex+=1
              rightIndex-=1
      #If the rightIndex cross the nth, leftIndex is the new pivot.
      if rightIndex < nth: leftPivot = leftIndex
      #If the leftIndex cross the nth, rightIndex is the new pivot.
      if nth < leftIndex: rightPivot = rightIndex
  return arr[nth]

if __name__ == "__main__":
  print("Find the nth element sorting out the list.")