# projection_engine.py

def project_growth(followers, engagement_rate, posts_per_week):

    # growth multiplier based on engagement
    engagement_factor = engagement_rate / 5

    # consistency multiplier
    consistency_factor = posts_per_week / 3

    growth_rate = 0.04 * engagement_factor * consistency_factor

    # conservative
    three_month_low = int(followers * (1 + growth_rate * 2))

    # base
    three_month_mid = int(followers * (1 + growth_rate * 3))

    # aggressive
    three_month_high = int(followers * (1 + growth_rate * 5))

    six_month = int(followers * (1 + growth_rate * 8))

    return {
        "3m_low": three_month_low,
        "3m_mid": three_month_mid,
        "3m_high": three_month_high,
        "6m": six_month
    }