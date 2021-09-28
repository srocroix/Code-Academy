class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = str(name)
    self.age = int(age)
    # add more parameters here
    self.sex = int(sex) 
    self.bmi = float(bmi)
    self.num_of_children = int(num_of_children)
    self.smoker = int(smoker)
    
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age -128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print(self.name + '\'s estimated insurance cost is ' + str(estimated_cost) + " dollars.")

  def update_age(self, new_age):
    self.age = new_age
    print(self.name + ' is now ' + str(self.age) + ' years old.')
    self.estimated_insurance_cost()

  def update_num_of_children(self, new_num_children):
    self.num_of_children = new_num_children
    if new_num_children < 2:
      print(self.name + ' has ' + str(self.num_of_children) + ' child.')
    else:
      print(self.name + ' has ' + str(self.num_of_children) + ' children.')
    self.estimated_insurance_cost()

  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print(self.name + ' has a BMI of ' + str(self.bmi) + '.')
    self.estimated_insurance_cost()

  def update_smoking_status(self, new_smoker):
    self.smoker = new_smoker
    if self.smoker == 0:
      print(self.name + ' is a non-smoker.')
    elif self.smoker == 1:
      print(self.name + ' is a smoker.')
    self.estimated_insurance_cost()

  def patient_profile(self):
    patient_information = {'Name': self.name, 'Age': self.age, 'Sex': self.sex, 'BMI': self.bmi, 'Number of Children': self.num_of_children, 'Smoker': self.smoker}
    return patient_information

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)
print('\n')
patient1.estimated_insurance_cost()
print('\n')
patient1.update_age(26)
print('\n')
patient1.update_num_of_children(1)
print('\n')
print(patient1.patient_profile())
print('\n')
patient1.update_bmi(23)
print('\n')
patient1.update_smoking_status(1)