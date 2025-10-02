BPR = float(input("bob what is your basic pay rate"))
RH = float(input("enter regular hours you work"))
BP = (BPR*RH)
print("your basic pay is:",BP)
OTH = float(input("enter overtime hours you work"))
OTP = BPR*1.5 * OTH
print("your overtime pay is:",OTP)
TP = OTP + BP
print("your total pay is:",TP)
