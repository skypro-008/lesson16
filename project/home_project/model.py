from datetime import date


class User:
    id: int
    first_name: str
    last_name: str
    age: int
    email: str
    role: str
    phone: str


class Order:
    id: int
    name: str
    description: str
    start_date: date
    end_date: date
    address: str
    price: int
    customer_id: int
    executor_id: int


class Offer:
    id: int
    order_id: int
    executor_id: int
