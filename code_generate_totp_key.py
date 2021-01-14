import pyotp

print("Put this code in const_private and in your totp generator app: " + pyotp.random_base32())
