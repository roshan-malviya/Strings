def dupli(stri):
	a={}

	for i in range(len(stri)):
		k=0

		for j in range(len(stri)):

			if stri[i]==stri[j]:
				k+=1
		a[stri[i]]=k-1
	return(a)


b=input()
print(dupli(b))