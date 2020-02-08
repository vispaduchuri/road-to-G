hasp=set()

def firstDuplicate(arr):
    for x in arr:
        if x in hasp:
            return (x)
        else:
            hasp.add(x)
      

duplicate = firstDuplicate([1,2,3,3,2,1])
print (duplicate)