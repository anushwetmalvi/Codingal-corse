Average_attendance = float(input("Enter the average attendance (in percentage): "))

if Average_attendance < 75:
    print("The student is not eligible for the exam based on attendance.")
    medical_certificate = input("Do you have a medical certificate? (yes/no): ")

    if medical_certificate.lower() == "yes":
        print("The student is eligible for the exam.")
    else:
        print("The student is not eligible for the exam.")
        print("They need at least 75% attendance or a valid medical certificate to be eligible.")
else:
    print("The student is eligible for the exam based on attendance.")