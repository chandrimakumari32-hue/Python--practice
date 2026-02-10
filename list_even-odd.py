# Taking input of list elements 
# count even and odd numbers in the list and give the sum.
my_list=[]
n=int(input("Enter total no. of  elements in list"))
for i in range(n):
  element=int(input("Enter elements of list"))
  my_list.append(element)
print(my_list)
even=0
odd=0
for a in my_list:
  if(a%2==0):
    even=even+1
  else:
    odd=odd+1
print("Total no. of even numbers:",even)
print("Total no. of odd numbers:",odd)
total=odd+even
print("Total elements counted:",total)
