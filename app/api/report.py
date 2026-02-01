from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.db.models import User, AgencyReview, RationaleLog
from app.db.deps import get_db
from app.api.deps import get_api_key
import csv
import io

router = APIRouter()

@router.get("/report/reviews/", dependencies=[Depends(get_api_key)])
def get_all_reviews(db: Session = Depends(get_db)):
    reviews = db.query(AgencyReview).all()
    return [
        {
            "review_id": r.id,
            "user_id": r.user_id,
            "reviewed_by": r.reviewed_by,
            "stage": r.review_stage,
            "result": r.review_result,
            "notes": r.notes,
            "created_at": r.created_at
        }
        for r in reviews
    ]

@router.get("/report/rationales/", dependencies=[Depends(get_api_key)])
def get_all_rationales(db: Session = Depends(get_db)):
    logs = db.query(RationaleLog).all()
    return [
        {
            "rationale_id": l.id,
            "entity_type": l.entity_type,
            "entity_id": l.entity_id,
            "reviewer_id": l.reviewer_id,
            "rationale": l.rationale,
            "created_at": l.created_at
        }
        for l in logs
    ]

@router.get("/report/reviews/csv/", dependencies=[Depends(get_api_key)])
def export_reviews_csv(db: Session = Depends(get_db)):
    reviews = db.query(AgencyReview).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["review_id", "user_id", "reviewed_by", "stage", "result", "notes", "created_at"])
    for r in reviews:
        writer.writerow([r.id, r.user_id, r.reviewed_by, r.review_stage, r.review_result, r.notes, r.created_at])
    return Response(content=output.getvalue(), media_type="text/csv")

@router.get("/report/rationales/csv/", dependencies=[Depends(get_api_key)])
def export_rationales_csv(db: Session = Depends(get_db)):
    logs = db.query(RationaleLog).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["rationale_id", "entity_type", "entity_id", "reviewer_id", "rationale", "created_at"])
    for l in logs:
        writer.writerow([l.id, l.entity_type, l.entity_id, l.reviewer_id, l.rationale, l.created_at])
    return Response(content=output.getvalue(), media_type="text/csv")