class Complex_Number:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def get_real(self):
        return self.real 
    def get_imag(self):
        return str(self.imag) + "i"
    def magnitude(self):
        return (self.real**2 + self.imag**2)**0.5
    def __add__(self,other):
        return Complex_Number(self.real+other.real,self.imag+other.imag)
    def __sub__(self,other):
        return Complex_Number(self.real-other.real,self.imag-other.imag)
    def  __mul__(self,other):
        return Complex_Number (((self.real*other.real)+(self.real*other.imag*-1)),((self.imag*other.real)+(self.imag*other.imag)))
    def __truediv__(self,other):
        return Complex_Number(self.real/other.real,self.imag/other.imag)

c1=Complex_Number(2,3)
c2=Complex_Number(5,7)
c3 = c1 + c2
c4 = c1 - c2
c5 = c1 * c2
c6 = c1 / c2

print(c3.real,c3.imag)
print(c4.real,c4.imag)
print(c5.real,c5.imag)
print(c6.real,c6.imag)

