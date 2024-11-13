                            # HOPITAL MANAGMENT PROGRAM ......

patients = []

print("\t****well come****\n******R.J.M MEDIICAL CENTER******")
help_request = input("How can we assist you? (1: Meet the doctor, 2: Admit a patient):")

while True:
   
    if help_request == '1':
        print("******************************")
        doctor_name = input("Which doctor would you like to meet? ")
        appointment_check = input(f"Have you taken an appointment with Dr.{doctor_name}? (yes/no): ")

        if appointment_check == 'no':
            print("Please take an appointment first.")
            schedule_response=input(f"woulf you like us to schedule an appoitment with Dr.{doctor_name}for you?(yes/no):")

            if schedule_response == "yes":
                print(f"scheduling your appointment with Dr.{doctor_name}....")
                print(f"doctor {doctor_name} timing: 10:00 AM to 1:00PM and 4:00PM to 7:00PM.")
                print("_______________________________")
                print("your appointment is now fixed.")
                print("_______________________________")
                print("**you may now meet the Doctor**\n\t**THANK YOU**")
                break
            else:
                print("please schedule an appointment and try again.")
                continue
        elif appointment_check == "yes":
            print(f"appintment with Dr.{doctor_name} confirmend. you may proceed.")
            print("\t**THANK YOU**\n**you may now meet the doctor.**")
            print("*******************************")
            break
        else:
            print("invalid response.")
            continue
    elif help_request == '2':
        print("Proceeding to patient admission.")
        print("________________________________")
    print("****************")
    print("1. Admit Patient")
    print("2. View Patients")
    print("3. Discharge patient")
    print("4. Exit")
    print("*****************")
    choice = input("Enter your choice (1/2/3/4):")

    
    if choice == '1':
        print("*************************")
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        disease = input("Enter patient disease: ")
        patients.append({'name': name, 'age': age, 'disease': disease})
        print("Patient admit successfully!")
        print("***************************")

    elif choice == '2':
        print("***************************")
        if not patients:
            print("No patients to display.")
        else:
            print("List of Patients:")
            for patient in patients:
                print(f"Name: {patient['name']}, Age: {patient['age']}, Disease: {patient['disease']}")
        print("*****************************")

    elif choice == '3':
            print("****************************")
            if not patients:
                print("No patients to discharge.")
            else:
                discharge_name = input("Enter the name of the patient to discharge: ")
                for patient in patients:
                    if patient['name']== discharge_name:
                        patients.remove(patient)
                        print(f"Patient {discharge_name} has been discharged.")
                        break
                else:
                    print(f"Patient {discharge_name} has not been in my hospital.")
            print("*****************************")

    elif choice == '4':
        print("**MAY ALLAH GIVE YOU GOOD HEALTH**.\n\t***** Goodbye******")
        break

    else:
        print("Invalid choice. Please try again.")