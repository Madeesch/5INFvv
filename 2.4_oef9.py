bedrag = float(input("Geef het bedrag: "))
bronvaluta = input("Geef de bronvaluta (EUR of USD): ")
doelvaluta = input("Geef de doelvaluta (EUR of USD): ")

wisselkoers = 1.18

bedrag_in_euro = bedrag / wisselkoers
bedrag_in_dollar = bedrag * wisselkoers

print(f"{bedrag} {bronvaluta} is gelijk aan {bedrag_in_dollar:.2f} {doelvaluta}")