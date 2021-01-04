from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

auction = {}
a = "yes"
while a == "yes":

  name = input("What is your name? ")
  amount = int(input("How much would you like to bid? $"))
 

  auction[name] = amount

  b = input("Any other bid?, Type 'yes' or 'no'.  ")
  if b == "yes":
    a = "yes"
    clear()
  elif b == "no":
    a = "no"


  #get the name[key] with the highest value
  c = max_key = max(auction, key=auction.get)
  
  #get the key[value] with the highest value
  all_values =  auction.values()
  max_value = max(all_values)
  clear()

print(f"{c} won the bid with ${str(max_value)}")