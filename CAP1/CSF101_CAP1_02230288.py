# https://k4y0x13.github.io/CSF101-Programming-Methodology/unit4/bubble-sort.html (Bubble sorting)
# https://k4y0x13.github.io/CSF101-Programming-Methodology/unit4/insertion-sort.html (Insertion sorting)
# https://k4y0x13.github.io/CSF101-Programming-Methodology/unit4/1-linear-search.html (Linear search)
# https://k4y0x13.github.io/CSF101-Programming-Methodology/unit4/2-binary-search.html (Binary search)
# https://k4y0x13.github.io/CSF101-Programming-Methodology/unit2/8.file-operations.html (writing the output file)

# Function to read the input file
def read_input_from_file(filename):
    students_scores = [] # Empty list to store the data
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()  # Removing the whitespaces present
        name_score = line.rsplit("_", 1)  # Split from the right side to separate name and scores
        name = name_score[0].strip()  # Get the name part and remove any additional whitespace
        scores = name_score[1].split(",")  # Split the second part(scores) by comma
        score = int(scores[1])  # Convert the second part(scores) to integer
        # Concatenate the number before the comma with the name
        full_name = f"{name}_{scores[0].strip()}"
         # Append a dictionary with the full name and score to the students_scores list
        students_scores.append({"name": full_name, "score": score})
    return students_scores


# Task 1: 
#Sorting algorithms

# Bubble sorting
def bubble_sort(students_scores):

    n = len(students_scores)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students_scores[j]["score"] > students_scores[j + 1]["score"]:
                # Swap if the current score is greater than the next
                students_scores[j], students_scores[j + 1] = students_scores[j + 1], students_scores[j]
    return students_scores

# Insertion sorting
def insertion_sort(students_scores):

    for i in range(1, len(students_scores)):
        key = students_scores[i]
        j = i - 1
        # Shift elements of the sorted part if they are larger than key
        while j >= 0 and students_scores[j]["score"] > key["score"]:
            students_scores[j + 1] = students_scores[j]
            j -= 1
        students_scores[j + 1] = key
    return students_scores

# Task 2:
# Searching algorithms

# Linear search
def linear_search(students_scores, target_score):
    results = []
    for student in students_scores:
        if student["score"] == target_score:
            results.append(student)
    return results

# Binary search
def binary_search(students_scores, target_score):
    low = 0
    high = len(students_scores) - 1
    results = []
    while low <= high:
        mid = (low + high) // 2
        if students_scores[mid]["score"] == target_score:
            results.append(students_scores[mid])
            # Check neighbors for duplicates with the same score
            i = mid - 1
            while i >= 0 and students_scores[i]["score"] == target_score:
                results.append(students_scores[i])
                i -= 1
            i = mid + 1
            while i < len(students_scores) and students_scores[i]["score"] == target_score:
                results.append(students_scores[i])
                i += 1
            break
        elif students_scores[mid]["score"] < target_score:
            low = mid + 1
        else:
            high = mid - 1
    return results

# Task 3:
# Calculating average score

# Function to calculate average score
def calculate_average(students_scores):
    total = sum(student["score"] for student in students_scores)
    return total / len(students_scores)

# Making a table to store the results 

# Function to print tables in formatted style
def print_table(title, data, output_file):
    output_file.write(f"{title}\n") # Writes the title of the table

    # Write the headers "Name" and "Score" for the table columns
    # { ljust(20) } ensures the "Name" column is left-aligned and takes up 20 characters of space
    # { ljust(5) } ensures the "Score" column is left-aligned and takes up 5 characters of space
    output_file.write("Name".ljust(20) + " | " + "Score".ljust(5) + "\n")


    # Write a line of dashes to separate the headers from the data
    # { '-' * 30 } creates a line of 30 dashes 
    output_file.write("-" * 30 + "\n")
    for item in data:

        # { ljust(30) } ensures the student's name is left-aligned and padded to 30 characters
        # { ljust(5) } ensures the score is left-aligned and padded to 5 characters
        # Write the formatted name and score for each student to the file
        output_file.write(f"{item['name'].ljust(20)} | {str(item['score']).ljust(5)}\n")
    
    # Adds an extra newline for spacing
    output_file.write("\n")


# Main function
def main():
    # Input file
    input_filename = '02230288.txt'
    
    # Read the input file
    students_scores = read_input_from_file(input_filename)
    
    # Task 1: 
    # Sorting using Bubble Sort and Insertion Sort
    bubble_sorted = bubble_sort(students_scores.copy())  # Use a copy to preserve original data
    insertion_sorted = insertion_sort(students_scores.copy())  # Use a copy to preserve original data
    
    # Task 2: 
    # Searching using Linear Search and Binary Search
    target_score = int(input("Enter the target score to search for: "))
    linear_search_results = linear_search(students_scores, target_score)
    binary_search_results = binary_search(bubble_sorted, target_score)  # Works on sorted data
    
    # Task 3: 
    # Calculating average score
    average_score = calculate_average(students_scores)
    
    # Task 4: 
    # Storing Search Results
    search_results = {
        "linear search": linear_search_results,
        "binary search": binary_search_results
    }
    
    # Task 5: 
    # Writing to output.txt
    output_filename = 'output.txt'
    with open(output_filename, 'w') as output_file:
        # Write the average score
        output_file.write(f"Average Score: {average_score:.2f}\n\n")
        
        # Write the sorted lists
        output_file.write("Bubble Sorted List:\n")
        print_table("", bubble_sorted, output_file)

        output_file.write("Insertion Sorted List:\n")
        print_table("", insertion_sorted, output_file)

        # Write the students scoring below and above average
        above_average = [s for s in students_scores if s["score"] > average_score]
        below_average = [s for s in students_scores if s["score"] < average_score]

        output_file.write("\nStudents Scoring Above Average:\n")
        print_table("Above Average Students", above_average, output_file)

        output_file.write("Students Scoring Below Average:\n")
        print_table("Below Average Students", below_average, output_file)


        # Find and write the lowest scores
        lowest_scores = bubble_sorted[0]["score"]
        lowest_students = [s for s in bubble_sorted if s["score"] == lowest_scores]
        output_file.write("Lowest Score(s):\n")
        print_table("Lowest Score Table", lowest_students, output_file)

        # Find and write the highest scores
        highest_scores = bubble_sorted[-1]["score"]
        highest_students = [s for s in bubble_sorted if s["score"] == highest_scores]
        output_file.write("Highest Score(s):\n")
        print_table("Highest Score Table", highest_students, output_file)


        # Write the search results
        output_file.write("\nSearch Results:\n")
        output_file.write("Linear Search Result:\n")
        output_file.write("")
        print_table("", linear_search_results, output_file)
        
        output_file.write("Binary Search Result:\n")
        print_table("", binary_search_results, output_file)

    print(f"Results have been written to {output_filename}.")

# Run the program
main()

