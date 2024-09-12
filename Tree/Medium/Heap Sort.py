                          # 25-08-24
class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        largest=i
        l=2*i+1
        r=2*i+2
        if l<n and arr[l]>arr[largest]:
            largest=l
        if r<n and arr[r]>arr[largest]:
            largest=r
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            self.heapify(arr,n,largest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        if n==0:
            return []
        if n==1:
            return arr
        for i in range((n-2)//2,-1,-1):
            self.heapify(arr,n,i)
            
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        for i in range(n-1,0,-1):
            arr[i],arr[0]=arr[0],arr[i]
            self.heapify(arr,i,0)
        return arr