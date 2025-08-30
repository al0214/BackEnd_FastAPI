from typing import Any, List, Optional
from pydantic import BaseSettings, ConfigDict, BaseModel
from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from models.users import User
from models.events import Event


# 데이터베이스 작업을 처리하는 클래스
class Database:
    
    # 클래스 초기화 시 모델을 인자로 받습니다 (예: User, Event)
    def __init__(self, model):
        self.model = model
        
    # 새 문서를 데이터베이스에 저장합니다.
    async def save(self, document) -> None:
        await document.create()
        return 
    
    # 주어진 ID를 이용해 문서를 조회합니다.
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        # 문서가 존재하면 반환, 없으면 False 반환
        if doc:
            return doc
        return False
    
    # 모든 문서를 리스트로 가져옵니다.
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    # 특정 ID의 문서를 업데이트합니다.
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        # Pydantic 모델을 딕셔너리로 변환
        des_body = body.dict()
        # 값이 None이 아닌 필드만 필터링하여 업데이트할 데이터를 만듭니다.
        des_body = {k:v for k,v in des_body.items() if v is not None}
        
        # MongoDB 업데이트 쿼리($set)를 생성합니다.
        update_query = {
            "$set": {
                field: value for field, value in des_body.items()
                    }
                }
        
        # 기존 문서를 가져옵니다.
        doc = await self.get(doc_id)
        # 문서가 존재하지 않으면 False 반환
        if not doc:
            return False

        # 문서에 업데이트 쿼리를 적용합니다.
        await doc.update(update_query)
        return doc
    
    # 특정 ID를 가진 문서를 삭제합니다.
    async def delete(self, id: PydanticObjectId) -> bool:
        # 먼저 문서를 조회합니다.
        doc = await self.get(id)
        # 문서가 존재하지 않으면 False를 반환합니다.
        if not doc:
            return False
        # 문서를 삭제합니다.
        await doc.delete()
        # 성공적으로 삭제했음을 나타내기 위해 True를 반환합니다.
        return True


# 환경 설정과 데이터베이스 초기화를 담당하는 클래스
class Settings(BaseSettings):
    
    # MongoDB 연결 URL (환경 변수에서 불러옴)
    DATABASE_URL: Optional[str] = None
    
    # 비동기적으로 데이터베이스를 초기화합니다.
    async def initialize_database(self):
        
        # MongoDB 클라이언트를 생성합니다.
        client = AsyncIOMotorClient(self.DATABASE_URL)
        
        # Beanie를 초기화하고 사용할 모델을 등록합니다.
        await init_beanie(database=client.get_default_database(),
                            document_models=[User, Event])
        
    # Pydantic 설정: .env 파일에서 환경 변수를 불러오고, 불필요한 변수는 무시합니다.
    model_config = ConfigDict(env_file='.env', extra="ignore")