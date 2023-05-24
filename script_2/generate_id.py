


tag_counts = {}
def generate_id(tag):
    """Génère un identifiant unique pour une balise en fonction de son type."""
    if tag not in tag_counts:
        tag_counts[tag] = 1
    else:
        tag_counts[tag] += 1
    return f"{tag}{tag_counts[tag]}"

# __________________________________________________________________________________________________________
