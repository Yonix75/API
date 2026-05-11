
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from models import DevilFruit
from db import fruits_collection

router = APIRouter()#ici cest cest mon groupe de routes


# @router.get("/")
# def get_fruits():
#     return {"fruits": "OK"}

def serialize(fruit): #ici on recupere des objet donc on les convertit en string pour les montrer et on suprime les objets
    fruit["id"] = str(fruit["_id"])
    del fruit["_id"]
    return fruit


# @router.get("/")
# def test():
#     return {"message": "ROUTE OK"}
    
 #!FastAPI gere le code http donc il gere le erreur HTTPException il arrete la fonction et return lerreur  
@router.post("/")
def create_fruit(fruit: DevilFruit):
    result = fruits_collection.insert_one(fruit.dict())
    new_fruit = fruits_collection.find_one({"_id": result.inserted_id})
    return serialize(new_fruit)


@router.get("/")
def get_fruits(type: str = None):#type is parametre void 
    query = {}#therme pour mango envoi moi tout
    #si type recois un parametre query le lira et me donnera se ce que je dommande
    if type:
        query["type"] = type
    
    fruits = fruits_collection.find(query) #find(la request) renvoi moi ce que je tai demander
    return [serialize(f) for f in fruits] #return la transfo des object en string

@router.get("/search")
def search_fruit(name: str):#ici param selon le nom
    fruit = fruits_collection.find_one({#trouve moi le fruit avec le nom
        "name": {"$regex": name, "$options": "i"}#option ignonre les maj et regex racourci la recherche du noom rechecher
    })
    
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    
    return serialize(fruit)


@router.put("/{id}")
def update_fruit(id: str, fruit: DevilFruit):
    # exclude_none : ne met a jour que les champs envoyes
    # Evite d'ecraser filename/roman_name avec None si non fournis
    update_data = {k: v for k, v in fruit.dict().items() if v is not None}
    
    result = fruits_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": update_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Fruit non trouve")
    
    updated = fruits_collection.find_one({"_id": ObjectId(id)})
    return serialize(updated)

@router.delete("/{id}")#insert id mango
def delete_fruit(id: str):
    result = fruits_collection.delete_one({"_id": ObjectId(id)})#selon lobject id quon donne en string et bien delete
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Fruit not found")
    
    return {"message": "delete"}
