######Run the script in your terminal to get new secret!
### python Sercretgenerate.py 
##Happy Play!


from django.utils.crypto import get_random_string
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_string(50, chars)
print SECRET_KEY
