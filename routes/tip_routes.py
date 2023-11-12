from fastapi import APIRouter, HTTPException
from config.db import conn
from bson import ObjectId
from models.tip import Tip
from schemas.tip_schema import tipEntity, entityList

tip_router = APIRouter()

@tip_router.get('/tips')
def find_all_tips():
    return entityList(conn.mydatabase.tips.find())

@tip_router.post('/tips')
def create_tip(tip: Tip):
    new_tip = dict(tip)
    if "id" in new_tip: del new_tip["id"]  # Eliminar id si está presente para evitar conflictos
    inserted_id = conn.mydatabase.tips.insert_one(new_tip).inserted_id
    return {"id": str(inserted_id)}

@tip_router.get('/tips/{id}')
def find_tip(id: str):
    tip = conn.mydatabase.tips.find_one({"_id": ObjectId(id)})
    if tip:
        return tipEntity(tip)
    else:
        raise HTTPException(status_code=404, detail="Tip not found")

@tip_router.put('/tips/{id}')
def update_tip(id: str, tip_data: Tip):
    tip = conn.mydatabase.tips.find_one({"_id": ObjectId(id)})
    if tip:
        update_data = tip_data.dict(exclude_unset=True)
        if "id" in update_data: del update_data["id"]
        conn.mydatabase.tips.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        return {"status": "Tip updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Tip not found")

@tip_router.delete('/tips/{id}')
def delete_tip(id: str):
    tip = conn.mydatabase.tips.find_one({"_id": ObjectId(id)})
    if tip:
        conn.mydatabase.tips.delete_one({"_id": ObjectId(id)})
        return {"status": "Tip deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Tip not found")

@tip_router.get('/tips/travel/{travel_id}')
def find_tips_by_travel(travel_id: int):
    tips = conn.mydatabase.tips.find({"travel": travel_id})
    return entityList(tips)