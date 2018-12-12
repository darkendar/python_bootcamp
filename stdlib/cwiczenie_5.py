import re

kody_pocztowe = re.compile("\d{2}\-\d{3}")
email = re.compile("\w*\@[a-z]*\.\D{2,3}")
data_ur = re.compile("[10-31]{2} [A-Z][a-z]{2} [1-2]\d{3}|[1-9] \D{3} [1-2]\d{3}")
#data_ur = re.compile("[1-31]{2} \D{3} [1-2]\d{3}")

wynik = kody_pocztowe.findall("gfhjgf02-345yug6f57 labla@blabla.comhjklh")
wynik_1 = email.findall("gfhjgf02-345yug6f57 labla@blabla.comhjklh jskj@@gmail.com siopio@1wer.coer ")
wynik_2 = data_ur.findall("gfhjgf02-345yug6f57 labla@blabla.comhjklhhiu342112 Jan 199008 Feb 304031Jul199235 Dec 192321 Jun 19504 Jan 194221 Dec 199KL9O1 Dec 1998")

print(wynik)
print(wynik_1)
print(wynik_2)
