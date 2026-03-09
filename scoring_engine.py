# scoring_engine.py

def calculate_growth_potential(followers, engagement_rate, posts_per_week):

    # Engagement score
    engagement_score = min(engagement_rate * 10, 100)

    # Posting consistency score
    consistency_score = min(posts_per_week * 10, 100)

    # Follower momentum
    if followers < 10000:
        follower_score = 80
    elif followers < 50000:
        follower_score = 70
    elif followers < 100000:
        follower_score = 60
    else:
        follower_score = 50

    growth_index = (
        0.4 * engagement_score +
        0.3 * consistency_score +
        0.3 * follower_score
    )

    return round(growth_index, 2)


def calculate_saturation_risk(niche):

    niche_saturation = {
        "Fitness": 80,
        "Tech": 70,
        "Travel": 65,
        "Education": 50,
        "Finance": 60,
        "Lifestyle": 75
    }

    return niche_saturation.get(niche, 60)


def calculate_consistency_score(posts_per_week):

    score = min(posts_per_week * 12, 100)
    return score


def calculate_monetization_readiness(followers, engagement_rate):

    score = (followers / 1000) * 2 + engagement_rate * 5

    return min(round(score, 2), 100)