
def findSum(lst, total):
  one = 0 
  two = len(lst)-1
  while two != 0:
    if lst[one] + lst[two] == total:
      return(lst[one], lst[two])
    if one == two:
      one = 0
      two = two-1
      print((one,two))
    one += 1
  return('total not found')
    

lst = [0,1,2,3,4]
total = 7
print(findSum(lst, 3))