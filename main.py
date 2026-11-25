# Hospital Billing and Patient Classification
# Concepts used: variables, data types, input/output, operators,
# conditional statements, and basic calculations.

print("========================================")
print("     HOSPITAL BILLING SYSTEM")
print("========================================")

# Patient details
patient_name = input("Enter patient name: ")
patient_age = int(input("Enter patient age: "))
patient_id = input("Enter patient ID: ")

print("\nEnter the charges:")
consultation_charge = float(input("Consultation charge: Rs. "))
diagnostic_charge = float(input("Diagnostic charge: Rs. "))
treatment_charge = float(input("Treatment charge: Rs. "))

# Validate age and charges
if patient_age <= 0:
    print("\nInvalid age. Age must be greater than zero.")
elif consultation_charge < 0 or diagnostic_charge < 0 or treatment_charge < 0:
    print("\nInvalid charges. Charges cannot be negative.")
else:
    # Calculate total before concession
    total_amount = consultation_charge + diagnostic_charge + treatment_charge

    # Apply concession based on patient category
    print("\nPatient categories:")
    print("1. General")
    print("2. Senior Citizen (60 years or above)")
    print("3. Student")

    category = int(input("Choose patient category (1/2/3): "))

    if category == 1:
        category_name = "General"
        concession_rate = 0
    elif category == 2:
        if patient_age >= 60:
            category_name = "Senior Citizen"
            concession_rate = 10
        else:
            category_name = "General (age condition not met)"
            concession_rate = 0
            print("Senior Citizen concession requires age 60 or above.")
    elif category == 3:
        category_name = "Student"
        concession_rate = 5
    else:
        category_name = "General (invalid category selected)"
        concession_rate = 0
        print("Invalid category. General billing will be applied.")

    # Concession is applied to the total bill
    concession_amount = total_amount * concession_rate / 100
    final_bill = total_amount - concession_amount

    # Payment details
    print("\nFinal bill amount: Rs.", round(final_bill, 2))
    amount_paid = float(input("Enter amount paid: Rs. "))

    if amount_paid < 0:
        print("\nInvalid payment. Payment cannot be negative.")
    elif amount_paid > final_bill:
        print("\nInvalid payment. Amount paid cannot exceed the final bill.")
    else:
        balance_amount = final_bill - amount_paid

        # Classify patient according to payment status
        if amount_paid == final_bill:
            payment_status = "Fully Paid"
        elif amount_paid > 0:
            payment_status = "Partially Paid"
        else:
            payment_status = "Unpaid"

        # Display billing receipt
        print("\n========================================")
        print("             BILLING RECEIPT")
        print("========================================")
        print("Patient Name       :", patient_name)
        print("Patient Age        :", patient_age)
        print("Patient ID         :", patient_id)
        print("Patient Category   :", category_name)
        print("----------------------------------------")
        print("Consultation Charge: Rs.", round(consultation_charge, 2))
        print("Diagnostic Charge  : Rs.", round(diagnostic_charge, 2))
        print("Treatment Charge   : Rs.", round(treatment_charge, 2))
        print("----------------------------------------")
        print("Total Amount       : Rs.", round(total_amount, 2))
        print("Concession Rate    :", concession_rate, "%")
        print("Concession Amount  : Rs.", round(concession_amount, 2))
        print("Final Bill         : Rs.", round(final_bill, 2))
        print("Amount Paid        : Rs.", round(amount_paid, 2))
        print("Balance Amount     : Rs.", round(balance_amount, 2))
        print("Payment Status     :", payment_status)
        print("========================================")
        print("        Thank you for visiting!")
        print("========================================")
