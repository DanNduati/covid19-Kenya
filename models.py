#!/usr/bin/python3
#database model
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    id = Column(INTEGER(11), primary_key=True)
    country_name = Column(String(5),nullable = False)
    total_cases = Column(INTEGER(255),nullable = False)
    new_cases = Column(INTEGER(255))
    total_deaths = Column(INTEGER(255))
    new_deaths = Column(INTEGER(255))
    total_recovered = Column(INTEGER(255))
    new_recovered = Column(INTEGER(255))
    active_cases = Column(INTEGER(255))
    serious_cases = Column(INTEGER(255))
    total_cases_per_m = Column(INTEGER(255))
    deaths_per_m = Column(INTEGER(255))
    total_tests = Column(INTEGER(255))
    tests_per_m = Column(INTEGER(255))
    population = Column(INTEGER(255))
    new_cases_per_m = Column(INTEGER(255))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))