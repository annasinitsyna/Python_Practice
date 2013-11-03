daily_donuts = raw_input("Please enter the number of donuts per day: ")
daily_donuts = int(daily_donuts)
people_number = raw_input ("Please neter the number of people: ")
people_number = int(people_number)
weekly_donuts = daily_donuts * 7
print people_number,'customers will need to eat',weekly_donuts / people_number,'per week in order to finish them all'
yearly_donuts = daily_donuts * 365
print 'An average American will eat',yearly_donuts / people_number,'per year'