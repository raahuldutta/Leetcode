def pivotedBinarySearch(arr, n, key): 
	pivot = findPivot(arr, 0, n-1);  
	if arr[pivot] == key: 
		return pivot 
	if arr[0] <= key: 
		return binarySearch(arr, 0, pivot-1, key); 
	return binarySearch(arr, pivot+1, n-1, key); 


def findPivot(arr, low, high): 
 
	mid = int((low + high)/2) 	
	if mid < high and arr[mid] > arr[mid + 1]: 
		return mid 
	if mid > low and arr[mid] < arr[mid - 1]: 
		return (mid-1) 
	if arr[low] >= arr[mid]: 
		return findPivot(arr, low, mid-1) 
	return findPivot(arr, mid + 1, high) 




def binarySearch(arr, low, high, key): 
	if high < low: 
		return -1	 
	mid = int((low + high)/2) 
	
	if key == arr[mid]: 
		return mid 
	if key > arr[mid]: 
		return binarySearch(arr, (mid + 1), high, 
											key); 
	return binarySearch(arr, low, (mid -1), key); 
 
arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3] 
n = len(arr1) 
key = 1
print("Index of the element is : ", 
	pivotedBinarySearch(arr1, n, key)) 
		
# This is contributed by Smitha Dinesh Semwal 
