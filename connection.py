# database/connection.py

from sqlalchemy import create_engine
DATABASE_URL = "mysql+pymysql://47VhtUGAurVFpEy.root:7X26JEm6wwejnHLM@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/Harvard?ssl_ca=<CA_PATH>&ssl_verify_cert=true&ssl_verify_identity=true" 

def get_engine():
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,   # handles dropped connections
        echo=False
    )
    return engine
