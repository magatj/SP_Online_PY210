
donors = [
    ["Michael Jordan", 500.00, 1, 500.00],
    ["Jeff Bezos", 877.33, 1, 877.33],
    ["William Gates, III", 653784.49, 2, 326892.24],
    ["Mark Zuckerberg", 16396.10, 3, 5465.37],
    ["Paul Allen", 708.42, 3, 236.14]
]



def menu():
    return input(
        "\nSelect an option number:"
        "\n1. Send a Thank You"
        "\n2. Create a Report"
        "\n3. Quit\n"
    )
	


def donor_list():
	for name in donors:
		print(name)
		

def add_to_list(new):
	new = (new,0,0,0) # changed new variable to include 3 more sets of values as initial value - could not find an easier way to donation amount after adding name.
	new = list(new)
	
	donors.append(new) #append donors list with new name along with the initial values of zeroes (place holder to fill all items in the list)
	
	
	return donors[-1] #go to latest donor
	
	
def add_donor(donor, amount): # created another function to insert user inputs for donations
	donor[2] = donor[2]+1 # add to previous number of donation
	donor[1] = donor[1] + int(amount)
	donor[3] = donor[1]/donor[2]
	
		

def Sort(val):
	return val[1]

	
def report():
	columns = ["Donor Name ", "|   Total Given |", "  Num Gifts", "| Average Gift   |"]
	donors_list1 = donors
	format1 = "{:<20}" + "{:^15}" + "{:^15}" + "{:^10}"
	format2= "{:<20}" + "${:^15.2f}" + "{:^15}" + "${:>13.2f}" # :> = right align -left it like this so it is more readable (could have left it blank)
	l = len(donors_list1)
	
	
	donors_list1 = donors_list1.sort(reverse = True, key =Sort)
	donors_list1 = donors
	
	
	
	
	print(format1.format(*columns))
	print('-' * 70)
	for i in range(l):
		print(format2.format(*donors_list1[i]))
	
	
	
	
def main():
	while True:
		user_selection = menu()
		if user_selection =='1':
			user_selection = input("\nPlease provide a full name to send thank you note or view list of donors: ")
			if user_selection.upper() == 'LIST':
				donor_list()
				continue
			for donor in donors: # connection with add_donor function
				if user_selection.upper() == donor[0].upper(): # See if donors are in the list
					new_donor = donor # new_donor is for any new donation for existing or new donors
					break
			else: # for new donors
				new_donor = add_to_list(user_selection.title())
			donation_amount = input("\nHow much {} willing to donate?: ".format(user_selection.title()))
			add_donor(new_donor, donation_amount) # from input of users input selection
			print("Thank you {}, for your generous donation of '${:.2f}!".format(new_donor[0], float(donation_amount)))
					
		if user_selection == '2':
			report()
		
		if user_selection == '3':
			break
		
		
		
		else:
			print('\n Please select a valid option')
			continue
	
if __name__ == '__main__':
    main()

	
	
	