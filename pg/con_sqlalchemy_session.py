#
# 1. Опишите критическую ошибку данной функции
# 2. Исправьте её
#


from sqlalchemy import MetaData, Table, Column, String, create_engine
from sqlalchemy.orm import sessionmaker
#from config import RemotePostgres
#from connector import create_session
#from models import RegistryObj, RegistryResource


def CopyNames():
    remote_engine = create_engine('postgresql+psycopg2://pguser:pgpwd@localhost:15432/de')
    RemoteSession = sessionmaker(bind=remote_engine)

    export_engine = create_engine('sqlite:///data.db', echo = True)
    metadata = MetaData()
    table_struct = Table(
                        'table_name',
                        metadata,
                        Column('uid', String(128), primary_key=True),
                        Column('name', String),
                    )
    metadata.create_all(export_engine)

    with export_engine() as session:
#        query = session.query(RegistryObj, RegistryResource).outerjoin(RegistryResource)
#        rows_count = session.query(RegistryObj).count()
        result = session.execute(table_struct.insert(), {'uid': '123', 'name': 'John'})

CopyNames()