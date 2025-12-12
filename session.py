from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dburl="sqlite:///./app.db"

engine=create_engine(dburl,connect_args={"check_same_thread":False})

localsess=sessionmaker(autocommit=False,autoflush=False,bind=engine)

