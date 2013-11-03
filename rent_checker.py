salary = raw_input("Enter your monthly salary: ")
salary = float(salary)
rent = raw_input("Enter your rent: ")
rent = float(rent)
percentage = (rent / salary) * 100
print "Your rent is %.2f" % percentage,"% of your monthly salary"
if percentage < 25:
    print "You are almost Donald Trump! Congratulations!"
elif percentage > 100:
	print "Trump is not impressed. How do you survive? o_0"
else:
	print "You are not living according to Donald Trump's rules"