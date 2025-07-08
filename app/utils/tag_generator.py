def enrich_tags(role, visual_tags, gps=None):
    role = role.lower()
    visual_tags = [tag.lower() for tag in visual_tags]

    # Default output
    final_tags = []

    # Rule examples (you can expand)
    if role == "bank officer":
        if "document" in visual_tags or "paper" in visual_tags:
            final_tags.append("Document Pickup")
        if "chair" in visual_tags or "desk" in visual_tags:
            final_tags.append("Client Office")
        if "man" in visual_tags or "person" in visual_tags:
            final_tags.append("KYC Visit")

    elif role == "delivery executive":
        if "package" in visual_tags or "box" in visual_tags:
            final_tags.append("Package Delivered")
        if "door" in visual_tags or "home" in visual_tags:
            final_tags.append("Client Home")
    
    elif role == "field agent":
        if "pen" in visual_tags or "signature" in visual_tags:
            final_tags.append("Form Filled")
        if "car" in visual_tags or "road" in visual_tags:
            final_tags.append("On-Site Visit")
    
    elif role == "surveyor":
        if "building" in visual_tags or "structure" in visual_tags:
            final_tags.append("Site Survey")
        if "helmet" in visual_tags:
            final_tags.append("Construction Visit")

    # Fallback tag if nothing matches
    if not final_tags:
        final_tags.append("General Field Visit")

    return final_tags
