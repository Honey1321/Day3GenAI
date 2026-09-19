class String:
  def text(self):
    text = input("Enter a string:")
    
    self.upper = text.upper()
    self.lower = text.lower()
    self.length = len(text)
    self.slice = text[2:7]
    self.strip = text.strip()
    self.count = text.count("o")
    self.find = text.find("good")
    
s = String()
s.text()

print("Upper:",s.upper)
print("Lower:",s.lower)
print("Length of the string:",s.length)
print("Slicing:",s.slice)
print("Removing space:",s.strip)
print("The number of 'o' present in the string is",s.count)
print("Found at the position ",s.find)
