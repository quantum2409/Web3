class bank:
    def __init__(self, name, fixed_rate_of_interest):
        self.name = name
    
    def check_hl(self, home_loan):
        if len(str(home_loan.aadn)) != 12 :
            print("Aadhar No. must be 12 digits long")
            return 0
        elif len(home_loan.PAN) != 10 :
            print("PAN No. invalid")
        elif int(home_loan.cred) <300 or int(home_loan.cred) >900:
            print("Credit score Invalid")
        elif int(home_loan.amount) > int(0.8*(int(home_loan.pv))) : #duration check 30
            print("Loan amount exceeds 80 percent of property value. Cant provide Loan.")
        elif int(home_loan.time) > 30 :
            print("Max time is 30yrs")
        else:
            print("Documents Verified")
            return 1
        return 0

    def check_p(self, personal):
        if len(str(personal.aadn)) != 12:
            print("Aadhar No. must be 12 digits long")
        elif len(personal.PAN) != 10 :
            print("PAN No. invalid")
        elif int(personal.cred) <300 or int(personal.cred) >900:
            print("Credit score Invalid")
        elif int(personal.amount) > 2.5*int(personal.in_pf):
            print("Loan amount exceeds 2.5*(annual income). Cant sanction loan.")
        elif int(personal.time) > 30 :
            print("Max time is 30yrs")
        else:
            print("Documents Verified")
            return 1
        return 0

class borrower:
    def __init__(self, name, aadhar_no, PAN, acc_no, credit_score, amount, time):
        self.name = name
        self.aadn = aadhar_no
        self.PAN = PAN
        self.accn = acc_no
        self.cred = credit_score
        self.amount = amount
        self.time = time
        print(f"Name: {self.name}\nAadhar No.: {self.aadn}\nPAN No.: {self.PAN}\nBank account no.: {self.accn}\nCredit No.: {self.cred}\n")

class home_loan(borrower):
    def __init__(self, name, aadhar_no, PAN, acc_no, credit_score, amount, time, prop_val):
        super().__init__(name, aadhar_no, PAN, acc_no, credit_score, amount, time)
        self.pv = prop_val

class personal(borrower):
    def __init__(self, name, aadhar_no, PAN, acc_no, credit_score, amount, time, income_proof):
        super().__init__(name, aadhar_no, PAN, acc_no, credit_score, amount, time)
        self.in_pf = income_proof

sbi = bank("SBI", 12)
na, adn, pn, acn, cs, lt, am, ti= input("Input \nName,\nAadhar no.,\nPAN no,\nAccount no. and \nCredit Score of the borrower followed by the \nLoan type needed(h for Home Loan and p for Personal loan), \nAmount of loan required and \nDuration of loan in years \nin this specified order\n").split()
if lt == 'h':
    pvt = int(input("Kindly mention the value of property(in INR) for which loan is being applied\n"))
    cst = home_loan(na, adn, pn, acn, cs, am, ti, pvt)
    ok1 = sbi.check_hl(cst)

elif lt == 'p':
    pvt = int(input("Kindly mention your annual income\n"))
    cst = personal(na, adn, pn, acn, cs, am, ti, pvt)
    ok1 = sbi.check_p(cst)

if ok1 ==1:
    inr = int(input("Acoording to prevailing lendind rates; Kindly enter a Valid Interest rate to be applied onto the loan in correspondance to its amount and duration.\n"))
    am_re = ((int(cst.amount))*(100+inr)/100)
    emi = float(am_re)/(int(cst.time) *12)
    agree = input(f'''Plz agree to following terms: 
    YOU AGREE to pay EMI of Rs {emi} on 5th day of every month until your outsatnding becomes 0. Kindly type 'yes' or 'no'. \n''')
    if agree == 'yes':
        print("Congratulations!!... The loan will be disbursed in 5-10 business days...")
    else:
        print("sorry the loan cud not be sanctioned")
