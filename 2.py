a1,a2,p,k=[],[],1,0
n=int(input("Enter size: "))

if n<2:
	print("Insufficient array size! Product not possible!")

else:
	print("Enter",n,"values:")

	for i in range(0,n):
		a1.append(int(input()))
		if a1[i]==0:
			k+=1
		if(a1[i]!=0):
			p=p*a1[i]

	if k==0:
		for i in range(0,n):
			a2.append(int(p/a1[i]))

	elif k==1:
		for i in range(0,n):
			if a1[i]==0:
				a2.append(p)
			else:
				a2.append(0)

	else:
		for i in range(0,n):
			a2.append(0)

	print("1st Array\n",a1,"\n2nd Array\n",a2)