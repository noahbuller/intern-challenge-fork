from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.utils.scoring import calculate_scoring_weights, calculate_social_media_factors, calculate_performance_factors, calculate_brand_compatability_factors
from app.models.SQLAlchemyModels import AthletesNew
from datetime import date
import json

router = APIRouter()

#API Endpoint to Get Athlete's Weighted Score
#Endpoint Type: GET
#Route URL: /api/v1/athletes/{athlete_id}/scoring_weights

@router.get("/athletes/{athlete_id}/scoring_weights")
async def calculate_athlete_score(athlete_id: str, db: Session = Depends(get_db)):
    athlete = db.query(AthletesNew).filter(AthletesNew.athlete_id == athlete_id).first()
    
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not found")
    
    performance_score = calculate_performance_factors(
        athlete.recent_results, athlete.improvement_trend, athlete.competition_level)
    
    social_media_score = calculate_social_media_factors(
        athlete.followers, athlete.engagement_rate, athlete.content_quality)
    
    brand_compatability_score = calculate_brand_compatability_factors(
        athlete.sports_relevance, athlete.audience_alignment, athlete.brand_values_match)
    
    weighted_score = calculate_scoring_weights(
        performance_score, social_media_score, brand_compatability_score)

    return {"weighted_score": weighted_score}




#API Endpoint to List All Athletes
#Endpoint Type: GET
#URL: /api/v1/athletes
@router.get("/athletes")
async def get_all_athletes(db: Session = Depends(get_db)):
    athletes = db.query(AthletesNew).all()
    return athletes

#API Endpoint to Get All Details for a Specific Athlete
#Endpoint Type: GET
#Route URL: /api/v1/athletes/{athlete_id}
@router.get("/athletes/{athlete_id}")
async def get_athlete(athlete_id: str, db: Session = Depends(get_db)):
    athlete = db.query(AthletesNew).filter(AthletesNew.athlete_id == athlete_id).first()
    
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not found")
    return athlete

#API Endpoint to Get Athlete Age
#Endpoint Type: GET
#Route URL: /api/v1/athletes/{athlete_id}/age
@router.get("/athletes/{athlete_id}/age")
async def get_athlete_age(athlete_id: str, db: Session = Depends(get_db)):
    athlete = db.query(AthletesNew).filter(AthletesNew.athlete_id == athlete_id).first()
    
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not found")
    if not athlete.date_of_birth:
        raise HTTPException(status_code=404, detail="Date of Birth not found")
    
    today = date.today()
    age = today.year - athlete.dob.year - ((today.month, today.day) < (athlete.dob.month, athlete.dob.day))
    return {"age": age}

