from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser
from pathlib import Path

conf_f = Path(__file__).parent.joinpath("config.ini")
config = ConfigParser()
config.read(conf_f)

user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'DOMAIN')
port = config.get('DEV_DB', 'PORT')
db = config.get('DEV_DB', 'DB_NAME')

URI = f"postgresql://{user}:{password}@{domain}:{port}/{db}"

engine = create_engine(URI, echo=True, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine)
session = DBSession()