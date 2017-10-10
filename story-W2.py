# let the user know what's going on
print ("Your Dream Vacation")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
name1 = raw_input("Enter your name: ")
name2 = raw_input("Enter your friend's name: ")
verb1 = raw_input("Enter a verb: ")
country = raw_input("Your favorite country: ")
transportation = raw_input("Your favorite mode of transportation: ")
adjective1 = raw_input("Enter an adjective: ")
adjective2 = raw_input("Enter another adjective: ")
adjective3 = raw_input("Enter one more adjective: ")
verb2 = raw_input("Enter another verb: ")
activity = raw_input("Your favorite hobby: ")
food = raw_input("Your favorite food: ")
noun1 = raw_input("Enter a noun: ")
noun2 = raw_input("Enter another noun: ")

# this is the story. it is made up of strings and variables.
story = "Once upon a time, " + name1 + " and " + name2 + " went on a dream vacation together while " + verb1 + " because they love " + country + " and especially traveling via " + transportation. " The " + adjective1 + adjective2 + adjective3 " adventure was thrilling because they love to " + verb2 + " and they really enjoy " + activity. " On their vacation, they ate lots of " + food + " with " + noun1 + " and " + noun2

# finally we print the story
print (story)
