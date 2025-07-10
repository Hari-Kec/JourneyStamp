from config import TAG_RULES

def generate_final_tags(visual_tags, role):
    visual_key = " ".join(sorted(set(tag.lower() for tag in visual_tags)))

    role_rules = TAG_RULES.get(role, {})
    matched_tag = None

    for key, tags in role_rules.items():
        if all(word.lower() in visual_key for word in key.split()):
            matched_tag = tags
            break

    if not matched_tag:
        if "package delivery bag" in visual_key:
            matched_tag = ["Package Delivered", "Client Doorstep", "Delivery Confirmation"]
        elif "document laptop chair" in visual_key:
            matched_tag = ["KYC Visit", "Form Filled", "Office Verification"]
        elif "gate nameplate house" in visual_key:
            matched_tag = ["Client Home", "Address Verified"]
        elif "tree mountain hill" in visual_key:
            matched_tag = ["Hiking", "Nature Trail", "Adventure"]
        elif "temple mosque church" in visual_key:
            matched_tag = ["Spiritual", "Religious Site Visit"]
        elif "selfie group" in visual_key:
            matched_tag = ["Selfie", "Team Photo", "Group Visit"]

    return matched_tag or ["General"]