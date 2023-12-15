import mysql.connector

def binary_search(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="farm_db"
)

# Create a cursor
mycursor = mydb.cursor()

# Execute SQL query
mycursor.execute("SELECT * FROM milk_production")

# Fetch results
myresult = mycursor.fetchall()
myresult_count = mycursor.rowcount

animal_numbers = [row[1] for row in myresult]

# Get the user's animal identification number
animal_number = int(input('Enter the animal identification number: '))

# Perform binary search
result = binary_search(animal_numbers, animal_number, 0, myresult_count - 1)

# Check the result of the search
if result != -1:
    print("\nThe animal record is at position", str(result), "in the database!")

    # Execute a new SQL query to retrieve specific data for the animal
    link = "SELECT * FROM milk_production WHERE identification = {}".format(animal_number)
    mycursor1 = mydb.cursor()
    mycursor1.execute(link)
    myresult1 = mycursor1.fetchall()

    # Display animal data
    for row in myresult1:
        print("Animal data below:")
        print(row)
else:
    print("The animal record was not found!")

# Close cursors and the database connection
mycursor.close()
mycursor1.close()
mydb.close()
