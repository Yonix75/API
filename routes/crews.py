
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from models import crews
from db import crews_collection

router = APIRouter()#ici cest cest mon groupe de routes


def serialize(crews): #ici on recupere des objet donc on les convertit en string pour les montrer et on suprime les objets
    crews["id"] = str(crews["_id"])
    del crews["_id"]
    return crews



 #!FastAPI gere le code http donc il gere l'erreur HTTPException il arrete la fonction et return lerreur  
@router.post("/")
def create_crew(fruit: crews):
    result = crews_collection.insert_one(fruit.dict())
    new_crew = crews_collection.find_one({"_id": result.inserted_id})
    return serialize(new_crew)



@router.get("/")
def get_crews(type: str = None):#type is parametre void 
    query = {}#therme pour mango envoi moi tout
    #si type recois un parametre query le lira et me donnera se ce que je dommande
    if type:
        query["type"] = type
    
    sagas = crews_collection.find(query) #find(la request) renvoi moi ce que je tai demander
    return [serialize(f) for f in sagas] #return la transfo des object en string


@router.get("/search")
def search_crew(name: str):#ici param selon le nom
    crew = crews_collection.find_one({#trouve moi le fruit avec le nom
        "name": {"$regex": name, "$options": "i"}#option ignonre les maj et regex racourci la recherche du noom rechecher
    })
    
    if not crew:
        raise HTTPException(status_code=404, detail="crew not found")
    
    return serialize(crew)

@router.put("/{id}")
def update_fruit(id: str, crew: crews):
    result = crews_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": crew.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Fruit non trouvé")#
    
    return {"message": "update"}



@router.delete("/{id}")#insert id mango
def delete_fruit(id: str):
    result = crews_collection.delete_one({"_id": ObjectId(id)})#selon lobject id quon donne en string et bien delete
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="crew not found")
    
    return {"message": "delete"}