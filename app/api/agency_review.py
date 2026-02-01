from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models import User, AgencyReview, RationaleLog
from app.db.deps import get_db
from app.api.deps import get_api_key
from pydantic import BaseModel

router = APIRouter()

class AgencyReviewRequest(BaseModel):
    user_id: int
    reviewed_by: int      # staff/counselor user id
    review_stage: str
    review_result: str    # approved, flagged, needs_more_info, blocked
    notes: str

class RationaleRequest(BaseModel):
    entity_type: str      # match, risk_flag, eligibility
    entity_id: int
    reviewer_id: int      # staff/counselor user id
    rationale: str

@router.post("/agency/review/", dependencies=[Depends(get_api_key)])
def agency_review(req: AgencyReviewRequest, db: Session = Depends(get_db)):
    reviewer = db.query(User).filter(User.id == req.reviewed_by).first()
    if not reviewer:
        raise HTTPException(status_code=404, detail="Reviewer not found")
    review = AgencyReview(
        user_id=req.user_id,
        reviewed_by=req.reviewed_by,
        review_stage=req.review_stage,
        review_result=req.review_result,
        notes=req.notes,
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return {"review_id": review.id, "status": review.review_result}

@router.post("/agency/rationale/", dependencies=[Depends(get_api_key)])
def add_rationale(req: RationaleRequest, db: Session = Depends(get_db)):
    reviewer = db.query(User).filter(User.id == req.reviewer_id).first()
    if not reviewer:
        raise HTTPException(status_code=404, detail="Reviewer not found")
    rationale = RationaleLog(
        entity_type=req.entity_type,
        entity_id=req.entity_id,
        reviewer_id=req.reviewer_id,
        rationale=req.rationale
    )
    db.add(rationale)
    db.commit()
    db.refresh(rationale)
    return {"rationale_id": rationale.id}