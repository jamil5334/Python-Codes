#class to convert Fahrenheit to celsius and vice versa
class Temperature
	def __init__(self,fahrenheit, celsius):
		self.fahrenheit=fahrenheit
		self.celsius=celsius

	def convert_fahrenheit(self):
		return(self.celsius*9/5)+32

	def convert_celsius(self):
		return(self.fahrenheit-32)*5/9

temp=Temperature(80,30)
print(temp.convert_fahrenheit())
print(temp.convert_celsius())