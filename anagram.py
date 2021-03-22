


def is_ana(stri1,stri2):
	if len(stri1)==len(stri2):
		k=0
		for i in stri1:
			if i in stri2:
				k+=1
		if k==len(stri1):
			return ('anagram')
		else:
			return('not anagram')
	else:
		return('not anagram')

a=input('first input')
b=input('second input')

print(is_ana(a,b))




