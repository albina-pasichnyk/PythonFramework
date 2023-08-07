from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from HW_21.models import product_model, base_model

engine = create_engine('postgresql://albinapasichnyk:new_password@localhost/albina_db', echo=True)
autocommit_engine = engine.execution_options(isolation_level='AUTOCOMMIT')

__session = sessionmaker(autocommit_engine)

base_model.Base.metadata.drop_all(engine)
base_model.Base.metadata.create_all(engine)

session: Session = __session()
