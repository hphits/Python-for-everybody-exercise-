text = "X-DSPAM-Confidence:    0.8475"
first= text.find('0')
last= text.find('5')
number=text[first:last+1]
print(float(number))
