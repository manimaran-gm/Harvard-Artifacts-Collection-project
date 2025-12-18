from sqlalchemy import (
    MetaData, Table, Column, Integer, Text, ForeignKey
)
from connection import get_engine

metadata = MetaData()

artifact_metadata = Table(
    "artifact_metadata", metadata,
    Column("id", Integer, primary_key=True),
    Column("title", Text),
    Column("culture", Text),
    Column("period", Text),
    Column("century", Text),
    Column("medium", Text),
    Column("dimensions", Text),
    Column("description", Text),
    Column("department", Text),
    Column("classification", Text),
    Column("accessionyear", Integer),
    Column("accessionmethod", Text)
)

artifact_media = Table(
    "artifact_media", metadata,
    Column("objectid", Integer, ForeignKey("artifact_metadata.id"), primary_key=True),
    Column("imagecount", Integer),
    Column("mediacount", Integer),
    Column("colorcount", Integer),
    Column("rank", Integer),
    Column("datebegin", Integer),
    Column("dateend", Integer)
)

artifact_colors = Table(
    "artifact_colors", metadata,
    Column("objectid", Integer, ForeignKey("artifact_metadata.id"), primary_key=True),
    Column("color", Text),
    Column("spectrum", Text),
    Column("hue", Text),
    Column("percent", Text),
    Column("css3", Text)
)

def create_tables():
    engine = get_engine()
    metadata.create_all(engine)
