#~/movie-service/app/database/movieDb.py

# import the required packages.
from importlib.metadata import metadata
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

#sqlite
# sqlalchemyDatabaseUrl = "sqlite:///./sql_app.db"

#postgresql
# sqlalchemyDatabaseUrl = "postgresql://user:password@postgresserver/db"

#mysql
sqlalchemyDatabaseUrl = "mysql+pymysql://root:root@127.0.0.1:3306/PlatformDatadb"

#Create engine instance
engine = create_engine(sqlalchemyDatabaseUrl)

#Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Session = scoped_session(SessionLocal)

#  create a Base class , use the function declarative_base() that returns a class
Base = declarative_base()

# database = Database(sqlalchemyDatabaseUrl)


def get_db():
    # now all calls to Session() will create a thread-local session
    dbConnectionSession = Session()
    try:
        yield dbConnectionSession
        dbConnectionSession.commit()
        dbConnectionSession.flush()
    except Exception:
        dbConnectionSession.rollback()
        # When an exception occurs, handle session session cleaning,
        # but raise the Exception afterwards so that user can handle it.
        raise
    finally:
        dbConnectionSession.close()
        Session.remove()


dbConn = get_db().__next__()
