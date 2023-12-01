import random
import string

class Password:
  def __init__(self, upperValue, lowerValue, digitValue):
    self.upperValue = upperValue
    self.lowerValue = lowerValue
    self.digitValue = digitValue
    self.length = upperValue + lowerValue + digitValue

  def generatePassword(self):
    upper_chars = string.ascii_uppercase
    lower_chars = string.ascii_lowercase
    digit_chars = string.digits

    upper_part = ''.join(random.choice(upper_chars) for _ in range(self.upperValue))
    lower_part = ''.join(random.choice(lower_chars) for _ in range(self.lowerValue))
    digit_part = ''.join(random.choice(digit_chars) for _ in range(self.digitValue))

    final_password = ''.join(random.sample(upper_part + lower_part + digit_part, self.length))

    return final_password

def main():
  print("\nGenerar contraseña Aleatoria")
  upperValue = int(input("\nIngrese la cantidad de mayusculas que desea: "))
  loweValue = int(input("\nIngrese la cantidad de minusculas que desea: "))
  digitValue = int(input("\nIngrese la cantidad de digitos"))

  password_generator = Password(upperValue, loweValue, digitValue)
  generated_password = password_generator.generatePassword()
  print(generated_password)

main()






