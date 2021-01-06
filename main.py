#Starting loop
while True:
  print("Type 1010101010 to end program")
  diameter = float(input("whats the diameter: ")) # User input(diameter)
  radius = diameter/2 # diamater/2 for easier calculations
  circum = (2*3.14*radius) # Calculates circumference
  area = (3.14*radius*radius) # Calculates area
  print(f"Circumference:{circum}, Area:{area}") # outputs calculations
  #Checking if exit number is typed
  if diameter == 1010101010:
    print("Exiting")
    break
