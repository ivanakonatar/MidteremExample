#konvertovati km u milje
kilometri=input("Unesite kilometre: ")

if not kilometri.isnumeric():
    print("Niste unijeli ispravan broj!")
    quit()

kilometri_float=float(kilometri)   #posto input vrati string pretvaramo u float (decimalni)

milje = kilometri_float*0.6213   #1 km ima 0.6213 milja

print(milje)
