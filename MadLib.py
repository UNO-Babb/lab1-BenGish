#MadLib.py
#Name: Ben Gish
#Date: 8/30/2024
#Assignment: MadLib.py

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input(" Give me a noun 1: ")
  noun2 = input(" Give me a noun 2: ")
  verb1 = input(" Give me verb 1: ")
  verb2 = input(" Give me verb 2: ")
  adjective1 = input(" Give me adjective 1: ")
  adjective2 = input(" Give me adjective 2: ")
  #Print the story with the user supplied words.
  print( noun1 + " goes to the park with " + noun2 + ". "+ noun1 + " " + verb1 + " to the " + adjective1 + " tree. " + noun2 + " " + verb2 + " over to " + noun1 + " " + "under the " + adjective2 + " tree. ") 


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
