from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.items import ItemCreate, ItemResponse
from app.services.items import create_item, get_item


router = APIRouter()


@router.post("/", response_model=ItemResponse)
def create_item_endpoint(
    payload: ItemCreate,
    owner_id: int = Query(default=1, ge=1),
    db: Session = Depends(get_db),
) -> ItemResponse:
    item = create_item(db, owner_id=owner_id, payload=payload)
    return item


@router.get("/{item_id}", response_model=ItemResponse)
def get_item_endpoint(item_id: int, db: Session = Depends(get_db)) -> ItemResponse:
    item = get_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return item
