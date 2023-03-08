date = input("Enter today's date (e.g. March 1, 2023 or 3-1-23): ")
mood = input("What is your mood on scale 1-10: ")
thoughts = input("Journal entry:\n")

with open(f"../journal/{date}.txt", 'w') as file:
    file.write(mood + 2 * '\n')
    file.write(thoughts)
