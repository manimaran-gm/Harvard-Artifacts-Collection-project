# queries/sql_queries.py

from sqlalchemy import text

SQL_QUERIES = {

    # ================= artifact_metadata =================
    "Artifacts from 11th century (Byzantine culture)": text("""
        SELECT *
        FROM artifact_metadata
        WHERE century = '11th century'
          AND culture = 'Byzantine';
    """),

    "Unique cultures represented": text("""
        SELECT DISTINCT culture
        FROM artifact_metadata
        WHERE culture IS NOT NULL;
    """),

    "Artifacts from the Archaic Period": text("""
        SELECT *
        FROM artifact_metadata
        WHERE period = 'Archaic Period';
    """),

    "Artifacts ordered by accession year (desc)": text("""
        SELECT title, accessionyear
        FROM artifact_metadata
        ORDER BY accessionyear DESC;
    """),

    "Artifact count per department": text("""
        SELECT department, COUNT(*) AS artifact_count
        FROM artifact_metadata
        GROUP BY department;
    """),

    # ================= artifact_media =================
    "Artifacts with more than 1 image": text("""
        SELECT objectid, imagecount
        FROM artifact_media
        WHERE imagecount > 1;
    """),

    "Average rank of artifacts": text("""
        SELECT AVG(rank) AS avg_rank
        FROM artifact_media;
    """),

    "Artifacts where colorcount > mediacount": text("""
        SELECT objectid, colorcount, mediacount
        FROM artifact_media
        WHERE colorcount > mediacount;
    """),

    "Artifacts created between 1500 and 1600": text("""
        SELECT objectid, datebegin, dateend
        FROM artifact_media
        WHERE datebegin >= 1500 AND dateend <= 1600;
    """),

    "Artifacts with no media files": text("""
        SELECT objectid
        FROM artifact_media
        WHERE mediacount = 0 OR mediacount IS NULL;
    """),

    # ================= artifact_colors =================
    "Distinct hues used": text("""
        SELECT DISTINCT hue
        FROM artifact_colors
        WHERE hue IS NOT NULL;
    """),

    "Top 5 most used colors": text("""
        SELECT color, COUNT(*) AS frequency
        FROM artifact_colors
        WHERE color IS NOT NULL
        GROUP BY color
        ORDER BY frequency DESC
        LIMIT 5;
    """),

    "Average color coverage percentage": text("""
        SELECT hue, AVG(CAST(percent AS DECIMAL(5,2))) AS avg_percent
        FROM artifact_colors
        WHERE percent IS NOT NULL
        GROUP BY hue;
    """),

    "Colors used for a given artifact (example ID = 1)": text("""
        SELECT *
        FROM artifact_colors
        WHERE objectid = 1;
    """),

    "Total color entries": text("""
        SELECT COUNT(*) AS total_color_entries
        FROM artifact_colors;
    """),

    # ================= JOIN QUERIES =================
    "Artifact titles and hues (Byzantine culture)": text("""
        SELECT m.title, c.hue
        FROM artifact_metadata m
        JOIN artifact_colors c ON m.id = c.objectid
        WHERE m.culture = 'Byzantine';
    """),

    "Artifact titles with associated hues": text("""
        SELECT m.title, c.hue
        FROM artifact_metadata m
        JOIN artifact_colors c ON m.id = c.objectid;
    """),

    "Artifacts with non-null period and media rank": text("""
        SELECT m.title, m.culture, me.rank
        FROM artifact_metadata m
        JOIN artifact_media me ON m.id = me.objectid
        WHERE m.period IS NOT NULL;
    """),

    "Top 10 ranked artifacts containing Grey hue": text("""
        SELECT m.title, me.rank
        FROM artifact_metadata m
        JOIN artifact_media me ON m.id = me.objectid
        JOIN artifact_colors c ON m.id = c.objectid
        WHERE c.hue LIKE '%Grey%'
        ORDER BY me.rank ASC
        LIMIT 10;
    """),

    "Artifact count and avg media count per classification": text("""
        SELECT m.classification,
               COUNT(*) AS artifact_count,
               AVG(me.mediacount) AS avg_media_count
        FROM artifact_metadata m
        JOIN artifact_media me ON m.id = me.objectid
        GROUP BY m.classification;
    """),

    # ================= CUSTOM QUERIES (EXTRA) =================
    "Top 10 classifications by artifact count": text("""
        SELECT classification, COUNT(*) AS total
        FROM artifact_metadata
        GROUP BY classification
        ORDER BY total DESC
        LIMIT 10;
    """),

    "Artifacts without culture information": text("""
        SELECT *
        FROM artifact_metadata
        WHERE culture IS NULL;
    """),

    "Artifacts acquired after 2000": text("""
        SELECT title, accessionyear
        FROM artifact_metadata
        WHERE accessionyear > 2000;
    """),

    "Artifacts with high image count (>5)": text("""
        SELECT m.title, me.imagecount
        FROM artifact_metadata m
        JOIN artifact_media me ON m.id = me.objectid
        WHERE me.imagecount > 5;
    """),

    "Most common acquisition methods": text("""
        SELECT accessionmethod, COUNT(*) AS count
        FROM artifact_metadata
        WHERE accessionmethod IS NOT NULL
        GROUP BY accessionmethod
        ORDER BY count DESC;
    """)
}
