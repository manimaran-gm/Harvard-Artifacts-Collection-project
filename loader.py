# etl/loader.py

from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError
from connection import get_engine
from schema import (
    artifact_metadata,
    artifact_media,
    artifact_colors
)

def load_data(metadata_rows, media_rows, color_rows):
    """
    Inserts transformed data into MySQL (TiDB Cloud)
    Prevents duplicates using primary key checks
    """

    engine = get_engine()

    with engine.begin() as connection:
        # ------------------ Deduplication ------------------
        existing_ids = set(
            row[0] for row in connection.execute(
                select(artifact_metadata.c.id)
            ).fetchall()
        )

        # Filter only new records
        new_metadata = [row for row in metadata_rows if row["id"] not in existing_ids]
        new_media = [row for row in media_rows if row["objectid"] not in existing_ids]
        new_colors = [row for row in color_rows if row["objectid"] not in existing_ids]

        # ------------------ Insert ------------------
        if new_metadata:
            connection.execute(insert(artifact_metadata), new_metadata)

        if new_media:
            connection.execute(insert(artifact_media), new_media)

        if new_colors:
            connection.execute(insert(artifact_colors), new_colors)

    return len(new_metadata)
