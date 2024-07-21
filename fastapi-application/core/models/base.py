from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import MetaData

from utils import camel_case_to_snake_case
from core.config import settings

class Base(DeclarativeBase):
    __abstract__ = True
    
    metadata = MetaData(
        naming_convention=settings.db.naming_convension
    )
    
    @declared_attr.directive
    def __tablename__(cls): 
        return f"{camel_case_to_snake_case(cls.__name__)}s"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    

