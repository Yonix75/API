
"""
Script à lancer UNE SEULE FOIS pour enrichir ta collection MongoDB
avec les images depuis api-onepiece.com.
 
Lance avec : python seed_images.py
"""
 
import requests
from db import fruits_collection
 
def seed_images():
    # 1. Récupère tous les fruits depuis l'API externe
    print("Récupération des fruits depuis api-onepiece.com...")
    response = requests.get("https://api.api-onepiece.com/v2/fruits/fr")
    
    if not response.ok:
        print(f"Erreur API: {response.status_code}")
        # Fallback : utilise les données locales (le JSON que tu as déjà)
        return seed_from_local()
    
    external_fruits = response.json()
    print(f"{len(external_fruits)} fruits récupérés depuis l'API externe")
    
    updated = 0
    not_found = 0
    
    for ext in external_fruits:
        filename = ext.get("filename") or ext.get("image")
        roman_name = ext.get("roman_name") or ext.get("romanName")
        
        if not filename or not roman_name:
            continue
        
        # Met à jour le fruit dans ta MongoDB qui a le même roman_name
        # et qui n'a pas encore de filename
        result = fruits_collection.update_many(
            {
                "roman_name": {"$regex": roman_name, "$options": "i"},
                "filename": {"$exists": False}  # seulement ceux sans image
            },
            {"$set": {"filename": filename}}
        )
        
        if result.modified_count > 0:
            updated += result.modified_count
            print(f"  ✓ {roman_name} → image ajoutée ({result.modified_count} doc(s))")
        else:
            not_found += 1
 
    print(f"\n✅ Terminé : {updated} fruits mis à jour, {not_found} sans correspondance")
 
 
def seed_from_local():
    """
    Fallback : utilise le JSON de tes données initiales
    (le fichier que tu avais partagé au début avec tous les fruits)
    """
    import json, os
    
    # Données extraites directement de ton JSON initial
    images_map = [
        {"roman_name": "Gomu Gomu no Mi",  "filename": "https://images.api-onepiece.com/fruits/5665e89442022d4c0e7684c650dc6d6b.png"},
        {"roman_name": "Bara Bara no Mi",  "filename": "https://images.api-onepiece.com/fruits/ce8729339b41da72e8e0f81dd7f71eee.png"},
        {"roman_name": "Sube Sube no Mi",  "filename": "https://images.api-onepiece.com/fruits/8eb2a1bcdebacd9077ce4881a2493e2d.png"},
        {"roman_name": "Kilo Kilo no Mi",  "filename": "https://images.api-onepiece.com/fruits/d11cc6067afe9f178c578d0871096bbd.png"},
        {"roman_name": "Bomu Bomu no Mi",  "filename": "https://images.api-onepiece.com/fruits/89ffd8470e61c97800e850ffc3bfe5c5.png"},
        {"roman_name": "Hana Hana no Mi",  "filename": "https://images.api-onepiece.com/fruits/5f82c2c5df83335a916f98dc3b09eade.png"},
        {"roman_name": "Doru Doru no Mi",  "filename": "https://images.api-onepiece.com/fruits/79c5de9660c570daf6e43b8c14df7ef6.png"},
        {"roman_name": "Baku Baku no Mi",  "filename": "https://images.api-onepiece.com/fruits/aa8f6a1e4770332fd38f90a71581ec79.png"},
        {"roman_name": "Toge Toge no Mi",  "filename": "https://images.api-onepiece.com/fruits/dbeda9afbf6c54e261d6a61e3e081751.png"},
        {"roman_name": "Supa Supa no Mi",  "filename": "https://images.api-onepiece.com/fruits/fbed871b2850a8feb187b5186a5a35ce.png"},
        {"roman_name": "Ito Ito no Mi",    "filename": "https://images.api-onepiece.com/fruits/0f40216451f24b2e66c9af2415f97548.png"},
        {"roman_name": "Yomi Yomi no Mi",  "filename": "https://images.api-onepiece.com/fruits/56fc9cdf59bcd8a6e53b3e7c31e11005.png"},
        {"roman_name": "Kage Kage no Mi",  "filename": "https://images.api-onepiece.com/fruits/de5dadf8502878ee5354b1c952b74f8b.png"},
        {"roman_name": "Nikyu Nikyu no Mi","filename": "https://images.api-onepiece.com/fruits/16cd53be2d987c15311b7f5e55deb3c2.png"},
        {"roman_name": "Jiki Jiki no Mi",  "filename": "https://images.api-onepiece.com/fruits/79014303ec2ac76ecdefdb8b19928fb9.png"},
        {"roman_name": "Ope Ope no Mi",    "filename": "https://images.api-onepiece.com/fruits/9e630a35c5acb817bfea06e65d72b661.png"},
        {"roman_name": "Shiro Shiro no Mi","filename": "https://images.api-onepiece.com/fruits/0dfd5dd587490832579f7ea6e3384e92.png"},
        {"roman_name": "Awa Awa no Mi",    "filename": "https://images.api-onepiece.com/fruits/07ea2172d8a86e7db1b8355778a3ff92.png"},
        {"roman_name": "Mera Mera no Mi",  "filename": "https://images.api-onepiece.com/fruits/a3a4f5f2d3b965e3836613b5d3036348.jpg"},
        {"roman_name": "Yami Yami no Mi",  "filename": "https://images.api-onepiece.com/fruits/d108706dfcaa5bcf3cddd184ddbb52a5.png"},
        {"roman_name": "Hito Hito no Mi",  "filename": "https://images.api-onepiece.com/fruits/28c479a3d76524452745f40bde7a0c37.png"},
        {"roman_name": "Uo Uo no Mi",      "filename": "https://images.api-onepiece.com/fruits/f640990d0f10e51a1bc097ffe6ab511c.jpg"},
        {"roman_name": "Inu Inu no Mi Moderu Okuchi no Makami", "filename": "https://images.api-onepiece.com/fruits/a3b44d115359ee0d7844ba8710ab4e08.png"},
    ]
    
    updated = 0
    for item in images_map:
        result = fruits_collection.update_many(
            {
                "roman_name": {"$regex": item["roman_name"], "$options": "i"},
                "filename": {"$exists": False}
            },
            {"$set": {"filename": item["filename"]}}
        )
        if result.modified_count > 0:
            updated += result.modified_count
            print(f"  ✓ {item['roman_name']} → {result.modified_count} doc(s) mis à jour")
    
    print(f"\n✅ {updated} fruits mis à jour")
 
 
if __name__ == "__main__":
    seed_images()