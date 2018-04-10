daily_donuts = raw_input("Please enter the number of donuts sold per day: ")
daily_donuts = int(daily_donuts)
people_number = raw_input ("Please enter the number of customers at a donut shop: ")
people_number = int(people_number)
weekly_donuts = daily_donuts * 7
print people_number,'customers will need to eat',weekly_donuts / people_number,'donuts each week in order to finish them all'
yearly_donuts = daily_donuts * 365
print 'A typical customer will eat',yearly_donuts / people_number,'donuts per year'
