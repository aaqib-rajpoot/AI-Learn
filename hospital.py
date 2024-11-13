patients = {}

print("******R.J.M MEDIICAL CENTER******")

while True:
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3/): ")

    if choice == '1':
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        disease = input("Enter patient disease: ")
        patients.append({'name': name, 'age': age, 'disease': disease})
        print("Patient added successfully!")

    elif choice == '2':
        if not patients:
            print("No patients to display.")
        else:
            print("List of Patients:")
            for patient in patients:
                print(f"Name: {patient['name']}, Age: {patient['age']}, Disease: {patient['disease']}")

    elif choice == '3':
        print("MAY ALLAH GIVE YOU GOOD HEALTH.\n***** Goodbye******")
        break

    else:
        print("Invalid choice. Please try again.")