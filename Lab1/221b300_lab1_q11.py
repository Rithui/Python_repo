# Input marks for five subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))

# Calculate aggregate marks and percentage
total_marks_obtained = subject1 + subject2 + subject3 + subject4 + subject5
maximum_marks_per_subject = 100 * 5  # Assuming 100 marks for each of the 5 subjects
percentage = (total_marks_obtained / maximum_marks_per_subject) * 100

# Print the results
print(f"Total marks obtained: {total_marks_obtained}")
print(f"Percentage obtained: {percentage:.2f}%")
