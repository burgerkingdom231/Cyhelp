# CyHelp Starter Code
cybersecurityBirthYear = 1970

# Greets user
print("Hello! I'm CyHelp.")
user = input("What is your name?\n")
print("Hello " + user + "! I'm here to help you learn about Cybersecurity!")

# Calculates how long cybersecurity has been around
currentyear = int(input("What is the current year?\n"))
timepass = currentyear - cybersecurityBirthYear
print("Wow, it has been " + str(timepass) + " years since Cybersecurity started!")

# Recounts start of Cybersecurity
print("\nThe field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")
input("Press enter to continue.")

# Describes Cybersecurity
print("\nCybersecurity refers to the practices that people use to protect computer systems and networks from cyber attacks.")
input("Press enter to continue.")
print("These people can be governments/nations, individuals, companies, community organizations, and hackers.")
input("Press enter to continue.")

# Introduces CIA Triad
print("\nThe CIA Triad is the model used to discuss cybersecurity. CIA stands for Confidentiality, Integrity, and Availability.")
# Get user's input and validate it
giveinfo = input("Would you like to learn more about the CIA Triad? Enter yes or no.\n").lower()

while giveinfo != "yes" and giveinfo != "no":
    print("Invalid input. Please enter yes or no.")
    giveinfo = input("Would you like to learn more about the CIA Triad? Enter yes or no.\n").lower()

# If user wants to learn more
if giveinfo == "yes":
    while True:
        answer = input("What would you like to learn more about? Enter the letter of the following options: (a) confidentiality, (b) integrity, (c) availability, or (d) none.\n").lower()

        while answer not in ["a", "b", "c", "d"]:
            print("Invalid input. Please enter a, b, c, or d.")
            answer = input("What would you like to learn more about? Enter the letter of the following options: (a) confidentiality, (b) integrity, (c) availability, or (d) none.\n").lower()

        if answer == "a":
            print("Confidentiality makes sure data is private.")
        elif answer == "b":
            print("Integrity makes sure data is accurate.")
        elif answer == "c":
            print("Availability makes sure data is accessible.")
        elif answer == "d":
            print("Thanks for chatting with me, and I hope you learned something new!")
            break
elif giveinfo == "no":
    print("Thanks for chatting with me, and I hope you learned something new!")

print("Goodbye! Stay safe online.")
