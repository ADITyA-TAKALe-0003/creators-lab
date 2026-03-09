# lever_detection.py

def detect_growth_levers(followers, engagement_rate, posts_per_week):

    primary_lever = ""
    secondary_lever = ""

    # Detect posting problem
    if posts_per_week < 3:
        primary_lever = "Posting Frequency"
        secondary_lever = "Content Consistency"

    # Detect engagement problem
    elif engagement_rate < 3:
        primary_lever = "Content Hook Quality"
        secondary_lever = "Audience Retention"

    # Detect scaling opportunity
    elif followers > 10000 and engagement_rate > 4:
        primary_lever = "Content Volume Scaling"
        secondary_lever = "Format Experimentation"

    else:
        primary_lever = "Content Optimization"
        secondary_lever = "Audience Interaction"

    return primary_lever, secondary_lever