ref=input("donner la reference :")
designation=input("donner la designation :")
prix=float(input("donner le prix unitaire :"))

quantite=int(input("donner la quantite en stock"))
valeur=prix * quantite


print("Reference:",ref)
print("Designation:",designation)
print("Prix unitaire:",prix,"DT")
print("Quantite en stock :",quantite)
print("valeur totale du stock :" ,valeur ,"DT")