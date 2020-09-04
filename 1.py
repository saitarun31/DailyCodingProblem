"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

n=int(input("enter range n: "))
k=int(input("enter k: "))
q=0
a=[]

print("Enter",n,"values")
for i in range(0,n):
 v=int(input())
 a.append(v)

for i in range(0,n):
 if(n<2):
  print("Sum not possible")
  q=1
  break
 for j in range(i+1,n):
  if a[i]+a[j]==k:
   print(a[i],"+",a[j],"=",k)
   q=1
  
if n<1 and q==0:
 print("Sum not possible")
elif q==0:
 print("No 2 elements sum equal to k")
