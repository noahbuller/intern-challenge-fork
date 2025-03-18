# Description: This file contains the SQLAlchemy models for the database schema.
# Import relationship based on database_schema.json
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Double, TIMESTAMP, JSON, UUID, func, UniqueConstraint, Index

# Import declarative base
from sqlalchemy.orm import declarative_base

# For connection with DBAPI implementations (Note: varchar is ~ the same as character varying)
from sqlalchemy.dialects.postgresql import VARCHAR

Base = declarative_base()

# Class for AthletesNew table --> has no foreign keys
class AthletesNew(Base):
    __tablename__ = 'athletes_new'
    athlete_id = Column(VARCHAR(12), primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    school = Column(VARCHAR(255), nullable=False)
    year = Column(VARCHAR(50), nullable=False)
    score = Column(Double, nullable=False)
    
    # __table_args__ = (
    #     UniqueConstraint('name', 'school', name='athletes_new_name_school_key'),
    #     Index('athletes_new_pkey', athlete_id, unique=True),
    # )

# Class for Athlete IG --> has no foreign key
class AthleteIG(Base):
    __tablename__ = 'athlete_ig'
    id = Column(VARCHAR(12), primary_key=True)
    handle = Column(VARCHAR(30), nullable=False)
    followers = Column(Integer, nullable=True)
    posts = Column(Integer, nullable=True)
    is_private = Column(Boolean, nullable=True)
    fetch_time = Column(TIMESTAMP(timezone=True), server_default=func.now())
    social_score = Column(Double, nullable=True)
    
    # __table_args__ = (
    #     Index('athlete_ig_pkey', id, unique=True),
    #     Index('idx_athlete_ig_id', id, handle),
    # )

# Class for athletes_media --> has foreign key of athlete_id from AthletesNew
class AthletesMedia(Base):
    __tablename__ = 'athletes_media'
    athlete_id = Column(VARCHAR(12), ForeignKey('athletes_new.athlete_id'), primary_key=True)
    headshot_url = Column(VARCHAR(255), nullable=True)
    
    # __table_args__ = (
    #     Index('athletes_media_pkey', athlete_id, unique=True),
    # )

# Class for Scores --> has foreign key of athlete_id from AthletesNew
class Scores(Base):
    __tablename__ = 'scores'
    score_id = Column(Integer, primary_key=True, autoincrement=True)
    athlete_id = Column(VARCHAR(12), ForeignKey('athletes_new.athlete_id'))
    season = Column(Integer, nullable=False)
    score = Column(Double, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    
    # __table_args__ = (
    #     UniqueConstraint('athlete_id', 'season', name='scores_athlete_season'),
    #     Index('scores_pkey', score_id, unique=True),
    # )

# Class for Brands --> has no foreign keys
class Brands(Base):
    __tablename__ = 'brands'
    brand_id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    name = Column(VARCHAR(100), nullable=False)
    logo_url = Column(VARCHAR(255), nullable=True)
    industry = Column(VARCHAR(50), nullable=True)
    website_url = Column(VARCHAR(255), nullable=True)
    create_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # __table_args__ = (
    #     UniqueConstraint('name', name='brands_name_key'),
    #     Index('brands_pkey', brand_id, unique=True),
    #     Index('idx_brands_name', name),
    # )

# Class for Signed_Athletes --> has foreign keys of athlete_id from AthletesNew
class SignedAthletes(Base):
    __tablename__ = 'signed_athletes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    athlete_id = Column(VARCHAR(12), ForeignKey('athletes_new.athlete_id'))
    brand_id = Column(VARCHAR(100), nullable=False)
    signed_date = Column(TIMESTAMP, server_default=func.now())
    contract_details = Column(JSON, nullable=True)

    # __table_args__ = (
    #     UniqueConstraint('athlete_id', 'brand_id', name='signed_athletes_athlete_id_brand_id_key'),
    #     Index('idx_signed_athletes_brand', brand_id),
    #     Index('signed_athletes_pkey', id, unique=True),
    # )

# Class for WatchListAthletes --> has foreign key of athlete_id from AthletesNew
class WatchListAthletes(Base):
    __tablename__ = 'watchlist_athletes'
    
    athlete_id = Column(VARCHAR(12), ForeignKey('athletes_new.athlete_id'), primary_key=True)
    brand_id = Column(VARCHAR(100), nullable=False, primary_key=True)  
    added_date = Column(TIMESTAMP, server_default=func.now())
    notes = Column(JSON)

    # __table_args__ = (
    #     UniqueConstraint('athlete_id', 'brand_id', name='watchlist_athletes_athlete_id_brand_id_key'),
    # )
