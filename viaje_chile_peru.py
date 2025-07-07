# viaje_chile_peru.py

import math

# Coordenadas aproximadas de algunas ciudades (latitud, longitud)
ciudades = {
    "Santiago": (-33.4489, -70.6693),
    "Arica": (-18.4783, -70.3126),
    "Iquique": (-20.2133, -70.1529),
    "Tacna": (-18.0066, -70.2463),
    "Lima": (-12.0464, -77.0428),
    "Arequipa": (-16.4090, -71.5375),
    "Cusco": (-13.5320, -71.9675)
}

# Velocidades promedio por transporte (en km/h)
velocidades = {
    "auto": 80,
    "bus": 60,
    "avión": 800
}

def calcular_distancia(coord1, coord2):
    # Fórmula del Haversine
    R = 6371  # radio de la Tierra en km
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    distancia_km = R * c
    return distancia_km

print("=== CALCULADORA DE VIAJE CHILE – PERÚ ===")

while True:
    origen = input("Ciudad de Origen (escriba 's' para salir): ").title()
    if origen.lower() == 's':
        print("Saliendo del programa.")
        break

    destino = input("Ciudad de Destino (escriba 's' para salir): ").title()
    if destino.lower() == 's':
        print("Saliendo del programa.")
        break

    if origen not in ciudades or destino not in ciudades:
        print("Una de las ciudades no está en la lista. Intente nuevamente.")
        print("Ciudades disponibles:", ", ".join(ciudades.keys()))
        continue

    print("Medios de transporte disponibles: auto, bus, avión")
    transporte = input("Seleccione el medio de transporte: ").lower()

    if transporte not in velocidades:
        print("Transporte no válido. Intente nuevamente.")
        continue

    coord_origen = ciudades[origen]
    coord_destino = ciudades[destino]
    distancia_km = calcular_distancia(coord_origen, coord_destino)
    distancia_millas = distancia_km * 0.621371
    velocidad = velocidades[transporte]
    duracion_horas = distancia_km / velocidad

    print(f"\n🛣️ De {origen} a {destino} en {transporte}:")
    print(f"📏 Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
    print(f"⏱️ Duración estimada: {duracion_horas:.2f} horas")
    print(f"📌 Narrativa del viaje: Desde {origen}, viajarás hacia {destino} en {transporte}, recorriendo aproximadamente {int(distancia_km)} kilómetros.\n")