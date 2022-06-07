import re
while True:
  password = input('Enter the Password: ')
  if (len(password)<8):
    print('The password must contain at least 8 Characters')
    continue
  elif not re.search("[a-z]", password):
    print('Password must contain the letters [a-z]')
    continue
  elif not re.search("[A-Z]", password):
    print('Password must contain the letters [A-Z]')
    continue
  elif not re.search("[0-9]", password):
    print('Password must contain [0-9]')
    continue
  elif not re.search("[_@$]", password):
    print('Password must contain [_@$]')
    continue
  elif re.search("\s", password):
    print('The password should not be written giving a space')
    continue
  else:
    print("Valid Password is", password)
    break