class QuickSort:
    def quicksort(self,arr):
        self.sort(arr,0,len(arr) - 1)
        return arr

    def sort(self,arr,left,right):
        if right <= left:
            return
        low = left
        high = right
        pivot = arr[low]
        while left < right :
            while left < right and arr[right] > pivot:
                right -= 1 
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot:
                left += 1 
            arr[right] = arr[left]
        arr[right] = pivot

        self.sort(arr,low,left-1)
        self.sort(arr,left+1,high)
  
    def quick_sort2(self,array, left, right):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right] > key:
                right -= 1
            array[left] = array[right]
            while left < right and array[left] <= key:
                left += 1
            array[right] = array[left]
        array[right] = key
        self.quick_sort2(array, low, left - 1)
        self.quick_sort2(array, left + 1, high)       

if __name__ == '__main__':
    S = QuickSort()
    

    #print(S.equalSubstring("abcd","bcdf",3))
    print(S.quicksort([4,2,7,4,9,5,7,0,1,12]))
            


        