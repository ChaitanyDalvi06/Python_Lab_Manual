countries = ["brazil", "russia", "india", "china", "srilanka" ]

member = input("Enter the name of the country: ").lower()

if member in countries:
	print(member, " is the member of BRICS")
else:
	print(member, " is not a member of BRICS")