
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
		

def add_to_list(new_donor):
	new = (new_donor,0,0,0)
	
	#-> insert condition here (inp statement) to fill up other 3 parameters
	new_a = '{},{:.2f},{:.0f},{:.2f}'.format(*new) #format tuple same as donors data format
	new_b = list([new_a]) # convert tuple to list
	new_a = new_b
	donors.append(new_b) #append donors with new name
	return donors[-1]
	
	
#def add_donor():
		
	
def report():
	columns = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
	donors_list1 = donors
	format1 = "{:12} |  " + "{:12} |  " + "{:5} |  " +"{:5}  |  "
	format2= "{:10}   " + "{:5}   " + "{:14}   " + "{:14}   "
	l = len(donors_list1)
	print(format1.format(*columns))
	print('-' * len(columns))
	#donors_list1.sort(reverse=True, key=lamba x, int(x[1]))
	for i in range(l):
		print(format2.format(*donors_list1[i]))
	#print(donors_list1)