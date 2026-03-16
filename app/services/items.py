from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.items import ItemCreate


def create_item(db: Session, owner_id: int, payload: ItemCreate) -> Item:
    item = Item(name=payload.name, description=payload.description, owner_id=owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_item(db: Session, item_id: int) -> Item | None:
    return db.query(Item).filter(Item.id == item_id).first()
