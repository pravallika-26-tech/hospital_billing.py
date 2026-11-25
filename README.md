# hospital_billing.py
Python Activity-Based Learning
Student Details
- Name: [SEELAM PRAVALLIKA NARASA]
- Roll Number: [N26V01A0330]
- Branch: [CSE)]
- Section: [4]
Titles of the 10 Selected Case Studies
1. Hospital Billing and Patient Classification
2. [Enter Case Study 2]
3. [Enter Case Study 3]
4. [Enter Case Study 4]
5. [Enter Case Study 5]
6. [Enter Case Study 6]
7. [Enter Case Study 7]
8. [Enter Case Study 8]
9. [Enter Case Study 9]
10. [Enter Case Study 10]
Replace the placeholders with your actual details and the titles of your ten selected case studies.

Case Study 1: Hospital Billing and Patient Classification
1. Problem Statement
Develop a Python program to process hospital consultation, diagnostic, and treatment charges. The program must apply conditional concessions, validate billing and payment constraints, calculate the final bill, and classify patients according to their payment status.
2. Objectives
- Accept patient details and hospital service charges.
- Calculate the total bill.
- Apply concessions according to the selected patient category.
- Validate age, charges, and payment amount.
- Calculate the balance amount.
- Classify patients as Fully Paid, Partially Paid, or Unpaid.
- Display a clear billing receipt.
3. Assumptions and Payment Policy
The assignment question does not specify concession percentages or a detailed payment policy. The following sample policy is used in this program:
1. General patients receive no concession.
2. Senior citizens aged 60 years or above receive a 10% concession.
3. Students receive a 5% concession.
4. If a person selects Senior Citizen but is younger than 60, the General category is applied.
5. Concession is calculated on the total consultation, diagnostic, and treatment charges.
6. Payment equal to the final bill is classified as Fully Paid.
7. Payment greater than zero but less than the final bill is classified as Partially Paid.
8. Payment of zero is classified as Unpaid.
9. Negative charges, invalid ages, negative payments, and payments greater than the final bill are rejected.
These are sample academic rules, not an actual hospital billing policy.
4. Algorithm
1. Start.
2. Read patient name, age, and patient ID.
3. Read consultation, diagnostic, and treatment charges.
4. Check whether age and charges are valid.
5. Calculate the total amount by adding all three charges.
6. Display the patient categories.
7. Read the selected category.
8. Apply the applicable concession percentage.
9. Calculate the concession amount.
10. Calculate the final bill.
11. Read the amount paid.
12. Validate the payment amount.
13. Calculate the balance amount.
14. Classify the payment as Fully Paid, Partially Paid, or Unpaid.
15. Display the billing receipt.
16. Stop.
5. Pseudocode
START
    INPUT patient_name, patient_age, patient_id
    INPUT consultation_charge
    INPUT diagnostic_charge
    INPUT treatment_charge

    IF patient_age <= 0 THEN
        DISPLAY "Invalid age"
    ELSE IF any charge is negative THEN
        DISPLAY "Invalid charges"
    ELSE
        total_amount = consultation_charge
                     + diagnostic_charge
                     + treatment_charge

        DISPLAY patient categories
        INPUT category

        IF category is General THEN
            concession_rate = 0
        ELSE IF category is Senior Citizen AND age >= 60 THEN
            concession_rate = 10
        ELSE IF category is Student THEN
            concession_rate = 5
        ELSE
            concession_rate = 0

        concession_amount = total_amount * concession_rate / 100
        final_bill = total_amount - concession_amount

        INPUT amount_paid

        IF amount_paid < 0 OR amount_paid > final_bill THEN
            DISPLAY "Invalid payment"
        ELSE
            balance = final_bill - amount_paid

            IF amount_paid = final_bill THEN
                status = "Fully Paid"
            ELSE IF amount_paid > 0 THEN
                status = "Partially Paid"
            ELSE
                status = "Unpaid"
            END IF

            DISPLAY billing receipt
        END IF
    END IF
STOP
6. Python Concepts Used
Python concept	Application in this program
Variables	Store patient details and billing amounts
Data types	String, integer, and float
Input and output	input() and print()
Arithmetic operators	Addition, subtraction, multiplication, and division
Relational operators	<, >, <=, and ==
Logical operators	or
Conditional statements	if, elif, and else
Type conversion	int() and float()
Built-in function	round()


7. Test Cases
Test	Category and age	Charges (consultation + diagnostic + treatment)	Amount paid	Expected result
1	General, 35	Rs. 1,000 + 2,000 + 3,000	Rs. 6,000	Fully Paid; final bill Rs. 6,000
2	Senior Citizen, 65	Rs. 1,000 + 2,000 + 3,000	Rs. 5,400	Fully Paid; 10% concession
3	Student, 20	Rs. 1,000 + 2,000 + 3,000	Rs. 2,000	Partially Paid; final bill Rs. 5,700
4	General, 40	Rs. 1,000 + 1,000 + 1,000	Rs. 0	Unpaid; balance Rs. 3,000
5	Senior Citizen, 45	Rs. 1,000 + 1,000 + 1,000	Rs. 3,000	General rate; no concession
6	General, 30	Negative consultation charge	Not requested	Invalid charges
7	General, 30	Rs. 1,000 + 1,000 + 1,000	Rs. 3,500	Invalid payment; exceeds bill


8. Sample Output
========================================
     HOSPITAL BILLING SYSTEM
========================================
Enter patient name: Ravi
Enter patient age: 65
Enter patient ID: H101

Enter the charges:
Consultation charge: Rs. 1000
Diagnostic charge: Rs. 2000
Treatment charge: Rs. 3000

Patient categories:
1. General
2. Senior Citizen (60 years or above)
3. Student
Choose patient category (1/2/3): 2

Final bill amount: Rs. 5400.0
Enter amount paid: Rs. 5400

========================================
             BILLING RECEIPT
========================================
Patient Name       : Ravi
Patient Age        : 65
Patient ID         : H101
Patient Category   : Senior Citizen
----------------------------------------
Consultation Charge: Rs. 1000.0
Diagnostic Charge  : Rs. 2000.0
Treatment Charge   : Rs. 3000.0
----------------------------------------
Total Amount       : Rs. 6000.0
Concession Rate    : 10 %
Concession Amount  : Rs. 600.0
Final Bill         : Rs. 5400.0
Amount Paid        : Rs. 5400.0
Balance Amount     : Rs. 0.0
Payment Status     : Fully Paid
========================================
        Thank you for visiting!
========================================
9. Conclusion
The Hospital Billing and Patient Classification program calculates hospital charges, applies category-based concessions, validates billing and payment values, and identifies the patient's payment status. It demonstrates the practical use of basic Python programming concepts in a hospital billing application.
10. How to Run
1. Install Python 3 on your computer.
2. Open the project folder in VS Code or another Python editor.
3. Open hospital_billing.py.
4. Run the program.
5. Enter patient details, charges, category, and payment when prompted.
6. Check the generated billing
