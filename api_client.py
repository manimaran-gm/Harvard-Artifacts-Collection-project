# etl/api_client.py

import requests

HARVARD_API_KEY = "7eb1d78f-86bc-49d1-aba8-12dce6a69098"


BASE_URL = "https://api.harvardartmuseums.org/object"

CLASSIFICATIONS = [
    'Accessories (non-art)',
    'Photographs',
    'Drawings',
    'Prints',
    'Paintings',
    'Sculpture',
    'Coins',
    'Vessels',
    'Textile Arts',
    'Archival Material',
    'Fragments',
    'Manuscripts',
    'Seals',
    'Straus Materials'
]

def fetch_artifacts_by_classification(classification, limit=2500):
    """
    Fetch exactly `limit` artifacts for a given classification
    """
    records = []
    page = 1
    size = 100  # max safe page size

    while len(records) < limit:
        params = {
            "apikey": HARVARD_API_KEY,
            "classification": classification,
            "page": page,
            "size": size
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()
        objects = data.get("records", [])

        if not objects:
            break

        records.extend(objects)
        page += 1

    return records[:limit]
