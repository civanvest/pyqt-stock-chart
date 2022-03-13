import pandas as pd
import sqlalchemy
from sqlalchemy.engine.base import Engine
import streamlit as st

class Database:

    def __init__(self, config: dict):
        self.config = config
        self.engine = self.connect()

    @st.cache(allow_output_mutation=True)
    def connect(self):
        user = self.config['user']
        password = self.config['password']
        host = self.config['host']
        port = self.config['port']
        dbname = self.config['dbname']
        engine = sqlalchemy.create_engine(
            f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
            )
        return engine

    @st.cache(hash_funcs={Engine: id})
    def run(self, query: str):
        result = pd.read_sql(query, self.engine)
        return result

    def __del__(self):
        self.engine.dispose()