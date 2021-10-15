from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:',
                       echo=True,
                       encoding="UTF-8")
engine.connect()

print(engine.execute("select 'hello'").scalar())