full_name = "Luigie Glinofria Sanchez"
year = 3
section = "BSCS 3A"
distance = 6.5
working_student = True

subjects = ["Computer Architecture and Organization", "Networking and Communication", "Machine Learning"]

print("--- STUDENT INFORMATION ---")
print("Full Name:", full_name)
print("Year Level:", year)
print("Section:", section)
print("Distance from Home to School:", distance, "km")
print("Working Student:", working_student)
print("Subjects:", subjects)

print("\n--- IF-ELSE ---")

if working_student:
    print(full_name, "is a working student.")
else:
    print(full_name, "is not a working student.")

print("\n--- FOR LOOP ---")

for subject in subjects:
    print("Subject:", subject)

print("\n--- WHILE LOOP ---")

current_year = 1

while current_year <= year:
    print("Completed/Current Year:", current_year)
    current_year += 1


print("\n--- MEMORY SIMULATION ---")

memory = [
    full_name,
    year,
    section,
    distance,
    working_student,
    subjects
]

print("Student information stored in memory:")

for index in range(len(memory)):
    print("Memory Location", index, ":", memory[index])

print("\nReading specific memory locations:")
print("Memory[0] - Full Name:", memory[0])
print("Memory[1] - Year:", memory[1])
print("Memory[2] - Section:", memory[2])
print("Memory[3] - Distance:", memory[3])
print("Memory[4] - Working Student:", memory[4])
print("Memory[5] - Subjects:", memory[5])


print("\n--- CPU AND MEMORY INTERACTION ---")
print("The CPU requests student data from memory.")
print("Memory provides the requested data to the CPU.")
print("CPU processes the data and displays the result.")