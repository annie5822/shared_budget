from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

DATABASE_URL = "mysql+mysqlconnector://shared_user:Annie58221!@localhost:3306/shared_budget"

# 建 engine（連到 MySQL）
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Base：所有資料表 class 都要繼承它
Base = declarative_base()

class User(Base):
    __tablename__ = "users"  # 這張表在 DB 裡就叫 users

    id = Column(Integer, primary_key=True, autoincrement=True)  # 使用者編號
    username = Column(String(50), unique=True, nullable=False)  # 帳號（不能重複）
    email = Column(String(100), unique=True, nullable=False)    # 信箱（也通常不重複）
    hashed_password = Column(String(255), nullable=False)       # 加密後的密碼
    created_at = Column(DateTime, default=datetime.utcnow)      # 建立時間
