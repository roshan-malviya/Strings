
def ispalindrome(stri):
	if stri==stri[::-1]:
		return 'Yes'

	else:
		return 'No !!'


a=input()

print(ispalindrome(a))