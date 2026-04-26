import uuid
#!La bibliothèque Pydantic est un outil très utilisé en Python pour valider, parser et structurer des données de façon automatique.
from pydantic import BaseModel#BaseModel sert à créer des modèles de données avec validation automatique.
from typing import Optional#Optional veut dire qu’une valeur peut être présente ou absente (None).
#!La bibliotheque typing Rendre le code plus lisible Détecter des erreurs plus tôt
class DevilFruit(BaseModel):
    name: str
    type: str
    power: str
    current_user: Optional[str] = None
    previous_user: Optional[str] = None
    description: Optional[str] = None
    
class crews(BaseModel):
    
 id : int
 name: str
 description: str
 status: str
 number: str
 roman_name: str
 total_prime: str
 is_yonko : str
