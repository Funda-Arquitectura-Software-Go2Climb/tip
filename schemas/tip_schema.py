def tipEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"],
        "travel": item["travel"]
    }

def entityList(entity) -> dict:
    return [tipEntity(item) for item in entity]
