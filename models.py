from sqlalchemy import Column, Integer, String, Date, Boolean, Text, ForeignKey, JSON, TIMESTAMP
from sqlalchemy.orm import relationship
from .session import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(100))
    dob = Column(Date)
    gender = Column(String(50))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    intake = relationship("EligibilityIntake", back_populates="user", uselist=False)

class EligibilityIntake(Base):
    __tablename__ = "eligibility_intake"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    marriage_intent = Column(Boolean, nullable=False)
    intake_status = Column(String(50))
    demographics = Column(JSON)
    life_stage = Column(String(100))
    intake_notes = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="intake")

class AgencyReview(Base):
    __tablename__ = "agency_review"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    reviewed_by = Column(Integer, ForeignKey("users.id"))
    review_stage = Column(String(50))
    review_result = Column(String(100))
    notes = Column(Text)
    created_at = Column(TIMESTAMP)

class RationaleLog(Base):
    __tablename__ = "rationale_log"
    id = Column(Integer, primary_key=True)
    entity_type = Column(String(50))
    entity_id = Column(Integer, nullable=False)
    reviewer_id = Column(Integer, ForeignKey("users.id"))
    rationale = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP)