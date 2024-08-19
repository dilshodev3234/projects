from sqlalchemy import BIGINT, CheckConstraint, create_engine, TEXT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.config import AbstractClass, Config


class Customer(AbstractClass):
    __tablename__ = "customers"
    id :Mapped[int] = mapped_column(BIGINT , autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT)
    lang : Mapped[str] = mapped_column()
    fullname : Mapped[str] = mapped_column()
    phone_number: Mapped[str] = mapped_column()
    role : Mapped[str] = mapped_column(default="CUSTOMER")
    tasks : Mapped[list['Task']] = relationship(back_populates='customer')

class Freelancer(AbstractClass):
    __tablename__ = "freelancers"
    id :Mapped[int] = mapped_column(BIGINT , autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT)
    lang : Mapped[str] = mapped_column()
    fullname : Mapped[str] = mapped_column()
    phone_number: Mapped[str] = mapped_column()
    category_id : Mapped[int] = mapped_column(ForeignKey("categories.id",ondelete="CASCADE"))
    role : Mapped[str] = mapped_column(default="FREELANCER")
    category : Mapped['Category'] = relationship(back_populates="freelancers")

class Category(AbstractClass):
    __tablename__ = "categories"
    id : Mapped[int] = mapped_column(BIGINT, autoincrement=True , primary_key=True)
    name : Mapped[str] = mapped_column()
    tasks : Mapped[list['Task']] = relationship(back_populates="category")
    freelancers : Mapped[list['Freelancer']] = relationship(back_populates="category")
#
class Task(AbstractClass):
    __tablename__ = "tasks"
    id : Mapped[int] = mapped_column(BIGINT, autoincrement=True , primary_key=True)
    title : Mapped[str] = mapped_column()
    price : Mapped[str] = mapped_column()
    description : Mapped[str] = mapped_column(TEXT)
    status : Mapped[str] = mapped_column(default="PROCESSING")
    customer_id : Mapped[int] = mapped_column(ForeignKey("customers.id",ondelete="CASCADE"))
    category_id : Mapped[int] = mapped_column(ForeignKey("categories.id",ondelete="CASCADE"))
    category : Mapped['Category'] = relationship(back_populates="tasks")
    customer : Mapped['Customer'] = relationship(back_populates="tasks")


