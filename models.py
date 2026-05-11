import uuid
#!La bibliothèque Pydantic est un outil très utilisé en Python pour valider, parser et structurer des données de façon automatique.
from pydantic import BaseModel#BaseModel sert à créer des modèles de données avec validation automatique.
from typing import Optional#Optional veut dire qu’une valeur peut être présente ou absente (None).
#!La bibliotheque typing Rendre le code plus lisible Détecter des erreurs plus tôt
class DevilFruit(BaseModel):
    name: str
    type: str
    power: Optional[str] = None
    roman_name: Optional[str] = None      # ← AJOUTÉ : nom japonais (Gomu Gomu no Mi...)
    filename: Optional[str] = None        # ← AJOUTÉ : URL de l'image
    current_user: Optional[str] = None
    previous_user: Optional[str] = None
    description: Optional[str] = None
class crews(BaseModel):
 crew_id: Optional[int] = None         # ancien champ "id" renommé pour éviter le conflit
 id : int
 name: str
 description: str
 status: str
 number: str
 roman_name: str
 total_prime: str
 is_yonko : str
