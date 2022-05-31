from replit import clear
#HINT: You can call clear() to clear the output in the console.
#The art is seperated from the while loop
# from art import logo

def bid_info(persons_name, bid_amount):
  #Write a code to make the user inputs stored inside a dictionary
  bidder_info[persons_name] = bid_amount
  bidder_name.append(name)


from art import logo2
print(logo2)
end_of_auction = False
bidder_info = {}
bidder_name = []


while end_of_auction == False:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  
  bid_info(persons_name=name, bid_amount=bid)
  
  direction = input("Are there any other bidders? Type 'yes or 'no'.")

  if direction == "no":
    end_of_auction = True
  else:
    clear()
    

#For debugging
# print(bidder_info)
# print(bidder_name)



highest_bid = 0
winner = ""

for i in bidder_info:
  bidder_value = bidder_info[i]
  if bidder_value >= highest_bid:
    winner = i
    highest_bid = bidder_value
  
  #For debugging
  # print(i)



result = f"The winner is {winner} with the highest bid of ${highest_bid}."
print(result)