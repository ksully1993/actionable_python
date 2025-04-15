# Script to calculate how many pizzas are needed for a given number of people using user input
# Includes some input error handling and is designed to restart on error or completion of script

import sys
import os
import math

from time import sleep

def main():
  print("Welcome to our Python Pizza Calculator!\nUse Ctrl+C at any time to exit.") #assumes script run from cmd line
  num_people = get_num_people()
  slices_per_person = get_slices_per_person()
  slices_per_pizza = get_slices_per_pizza()
  num_slices = num_people * slices_per_person # total number of slices needed
  #next time will use math.ceil to calculate total pizzas needed
  num_pizzas_w_remainder = calc_pizzas(num_slices, slices_per_pizza) #calculates number of whole pizas needed
  print("You need ", num_pizzas_w_remainder[0], " pizzas to feed ", num_people, " people.")
  print("There will be ", num_pizzas_w_remainder[1], " leftover slices.")
  restart_script()

#Get number of people to feed as an int, restart if incorrect input.
def get_num_people(): 
  num_people = input("\nHow many people are eating? ")
  try:
    int(num_people)
    num_people = int(num_people)
    return num_people
  except ValueError:
    print("\nValue must be an integer. Please try again!")
    restart_script()
    
#Get number of slices per person to feed as a float rounded to 1 decimal place.
def get_slices_per_person(): 
  slices_per_person = round(float(input("\nHow many slices per person? ")),1)
  return slices_per_person

#Get number of slices in each pizza as an integer, restart if incorrect input.
def get_slices_per_pizza():
  slices_per_pizza = input("\nHow many slices per pizza? ") # should be an int
  # Checks if input is int before updating value, restart script on error
  try:
    int(slices_per_pizza)
    slices_per_pizza = int(slices_per_pizza)
    return slices_per_pizza
  except ValueError:
    print("\nValue must be an integer. Please try again!")
    restart_script()

#Take number of slices and slices per pizza as input to calculate number of whole pizzas needed.
#Also returns number of lslices left in the final pizza after everyone is fed.
#next time will use math.ceil to calculate total pizzas needed
def calc_pizzas(num_slices, slices_per_pizza):
  num_pizzas = num_slices / slices_per_pizza
  remaining_slices_needed = num_slices % slices_per_pizza
  leftover_slices = 0
  if remaining_slices_needed: #calculates what portion of a whole pizza needed
    num_pizzas += 1
    leftover_slices = slices_per_pizza - remaining_slices_needed
  return math.trunc(num_pizzas), leftover_slices #convert num_pizzas to int before returning

#Restart script with a 3 second delay
#os.exec* releases all resources associated with the previous script instance
def restart_script():
  print("\nRestarting script...")
  for i in range(3,0,-1): #countdown from 3 to 1 before restarting
    sleep(1.0) #wait 1 second
    print(i, "...", sep="")
  os.execv(sys.executable, ['python3'] + sys.argv) # restart script

main()
