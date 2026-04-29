nota = float(input("Ingrese una nota entre 1.0 y 7.0:"))
if nota < 4.0:
   print("estas reprobado")
elif nota >= 4.0 and nota <= 5.9:
   print("estas aprobado")
elif nota>5.9 and nota <=7.0:
   print("eres destacado")
else:
   print("no puedes sobrepasar la nota arriba de 7.0")
   
   