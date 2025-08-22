from sqlmodel import SQLModel, Session, create_engine
from models.events import Event # Event 모델이 정의된 파일 경로
from NonCommit.password import mypassword


# MySQL 연결 정보
mysql_user = "al0214"
mysql_password = mypassword()
mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_db = "planner_db"

database_connection_string = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"

engine_url = create_engine(database_connection_string, echo=True)

def conn():
    """데이터베이스에 테이블을 생성하는 함수"""
    SQLModel.metadata.create_all(engine_url)

def get_session():
    """
    데이터베이스 세션을 직접 반환하는 함수.
    호출하는 곳에서 세션을 닫아줘야 합니다.
    """
    with Session(engine_url) as session:
        yield session