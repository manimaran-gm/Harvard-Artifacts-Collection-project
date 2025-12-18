# etl/transformer.py

def transform_artifacts(raw_records, classification):
    """
    Transforms raw API records into structured data
    for artifact_metadata, artifact_media, artifact_colors
    """

    metadata_rows = []
    media_rows = []
    color_rows = []

    for record in raw_records:
        object_id = record.get("id")

        # ---------------- artifact_metadata ----------------
        metadata_rows.append({
            "id": object_id,
            "title": record.get("title"),
            "culture": record.get("culture"),
            "period": record.get("period"),
            "century": record.get("century"),
            "medium": record.get("medium"),
            "dimensions": record.get("dimensions"),
            "description": record.get("description"),
            "department": record.get("department"),
            "classification": classification,
            "accessionyear": record.get("accessionyear"),
            "accessionmethod": record.get("accessionmethod")
        })

        # ---------------- artifact_media ----------------
        media_rows.append({
            "objectid": object_id,
            "imagecount": record.get("imagecount"),
            "mediacount": record.get("mediacount"),
            "colorcount": record.get("colorcount"),
            "rank": record.get("rank"),
            "datebegin": record.get("datebegin"),
            "dateend": record.get("dateend")
        })

        # ---------------- artifact_colors (AGGREGATED) ----------------
        colors = record.get("colors", [])

        if colors:
            color_rows.append({
                "objectid": object_id,
                "color": ",".join([c.get("color") for c in colors if c.get("color")]),
                "spectrum": ",".join([c.get("spectrum") for c in colors if c.get("spectrum")]),
                "hue": ",".join([c.get("hue") for c in colors if c.get("hue")]),
                "percent": ",".join([str(c.get("percent")) for c in colors if c.get("percent") is not None]),
                "css3": ",".join([c.get("css3") for c in colors if c.get("css3")])
            })
        else:
            color_rows.append({
                "objectid": object_id,
                "color": None,
                "spectrum": None,
                "hue": None,
                "percent": None,
                "css3": None
            })

    return metadata_rows, media_rows, color_rows
