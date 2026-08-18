def binary_search(a,x):\n    lo,hi=0,len(a)-1\n    while lo<=hi:\n        mid=(lo+hi)//2\n        if a[mid]==x: return mid\n        if a[mid]<x: lo=mid+1\n        else: hi=mid-1\n    return -1
