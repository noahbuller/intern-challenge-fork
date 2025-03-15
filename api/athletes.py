from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from utils.scoring import calculate_scoring_weights, calculate_social_media_factors, calculate_performance_factors, calculate_brand_compatability_factors
from models.SQLAlchemyModels import AthletesNew

router = APIRouter()

#Define a GET route from the FastAPI
@router.get("/athletes/{athlete_id}/score")
async def get_athlete_score(athlete_id: str, db: Session = Depends(get_db)):
    
    athlete = db.query(AthletesNew).filter(AthletesNew.athlete_id == athlete_id).first()
    
    if not athlete: #check if athlete with provided id exists
        raise HTTPException(status_code=404, detail="Athlete not found")
    