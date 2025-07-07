# verificar_asn.py

asn = input("Ingrese el número de AS: ")

if asn.isdigit():
    asn = int(asn)

    if 64512 <= asn <= 65534:
        print("El ASN es PRIVADO.")
    elif 4200000000 <= asn <= 4294967294:
        print("El ASN es PRIVADO.")
    else:
        print("El ASN es PÚBLICO.")
else:
    print("Debe ingresar un número entero válido.")