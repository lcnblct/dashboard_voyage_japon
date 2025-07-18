# Coordonnées des villes japonaises

def get_city_coords(city):
    """Retourne les coordonnées (latitude, longitude) d'une ville japonaise"""
    coords = {
        "Tokyo": (35.6895, 139.6917),
        "Kyoto": (35.0116, 135.7681),
        "Osaka": (34.6937, 135.5023),
        "Hiroshima": (34.3853, 132.4553),
        "Nara": (34.6851, 135.8048),
        "Sapporo": (43.0621, 141.3544),
        "Fukuoka": (33.5902, 130.4017),
        "Nagoya": (35.1815, 136.9066),
        "Kobe": (34.6901, 135.1955),
        "Yokohama": (35.4437, 139.6380),
        "Kamakura": (35.3192, 139.5467),
        "Hakone": (35.2323, 139.1067),
        "Nikko": (36.7500, 139.6167),
        "Takayama": (36.1461, 137.2522),
        "Kanazawa": (36.5613, 136.6562),
        "Matsumoto": (36.2380, 137.9720),
        "Nagano": (36.6489, 138.1950),
        "Sendai": (38.2688, 140.8721),
        "Matsuyama": (33.8416, 132.7660),
        "Kumamoto": (32.8031, 130.7079),
        "Kagoshima": (31.5602, 130.5581),
        "Okinawa": (26.2124, 127.6809),
        "Naha": (26.2124, 127.6809),
        "Shizuoka": (34.9769, 138.3831),
        "Okayama": (34.6618, 133.9344),
        "Kurashiki": (34.5854, 133.7722),
        "Himeji": (34.8164, 134.7000),
        "Miyajima": (34.2994, 132.3219),
        "Ishigaki": (24.3448, 124.1570),
        "Kushiro": (42.9750, 144.3747),
        "Asahikawa": (43.7706, 142.3650),
        "Akita": (39.7200, 140.1025),
        "Aomori": (40.8243, 140.7400),
        "Niigata": (37.9022, 139.0232),
        "Toyama": (36.6953, 137.2113),
        "Fukui": (36.0652, 136.2217),
        "Tottori": (35.5011, 134.2351),
        "Shimane": (35.4723, 133.0505),
        "Yamaguchi": (34.1783, 131.4736),
        "Tokushima": (34.0658, 134.5593),
        "Kochi": (33.5588, 133.5311),
        "Ehime": (33.8416, 132.7660),
        "Oita": (33.2381, 131.6126),
        "Miyazaki": (31.9111, 131.4239),
        "Saga": (33.2494, 130.2988),
        "Nagasaki": (32.7503, 129.8779)
    }
    
    # Recherche insensible à la casse
    city_lower = city.lower().strip()
    for key, value in coords.items():
        if key.lower() == city_lower:
            return value
    return (None, None)

def get_supported_cities():
    """Retourne la liste des villes supportées"""
    return [
        "Tokyo", "Kyoto", "Osaka", "Hiroshima", "Nara", "Sapporo", "Fukuoka", 
        "Nagoya", "Kobe", "Yokohama", "Kamakura", "Hakone", "Nikko", "Takayama", 
        "Kanazawa", "Matsumoto", "Nagano", "Sendai", "Matsuyama", "Kumamoto", 
        "Kagoshima", "Okinawa", "Naha", "Shizuoka", "Okayama", "Kurashiki", 
        "Himeji", "Miyajima", "Ishigaki", "Kushiro", "Asahikawa", "Akita", 
        "Aomori", "Niigata", "Toyama", "Fukui", "Tottori", "Shimane", 
        "Yamaguchi", "Tokushima", "Kochi", "Ehime", "Oita", "Miyazaki", 
        "Saga", "Nagasaki"
    ] 