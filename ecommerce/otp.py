import random


# GENERATE OTP
class OTP:
   def __init__(self):
      self.number = "012345"
      self.otp = " "

   def code_otp(self):
      for i in range(6):
         self.otp += random.choice(self.number)
      print(f"Your OTP {self.otp}")

run_otp = OTP()
run_otp.code_otp()