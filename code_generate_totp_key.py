import pyotp
import pyqrcode

key = pyotp.random_base32()
uri = pyotp.totp.TOTP(key).provisioning_uri(name='Shelly Telegram Bot', issuer_name='')

print("Put this code in const_private and in your totp generator app: " + key)
print(pyqrcode.create(uri).terminal(quiet_zone=2))
