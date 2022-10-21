from sqlalchemy import create_engine, MetaData
#conectando a la base de datos
engine = create_engine("mysql+pymysql://root:@localhost:3306/storedb")

meta = MetaData()
conn = engine.connect()
