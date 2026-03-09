import os
from groq import Groq


def generate_ai_strategy(
    followers,
    engagement_rate,
    posts_per_week,
    niche,
    content_format,
    growth_index,
    primary_lever,
    projection_mid
):

    try:

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        prompt = f"""
You are an expert creator growth strategist.

Analyze the following creator profile and provide strategic advice.

Creator Profile:
Followers: {followers}
Engagement Rate: {engagement_rate}%
Posts Per Week: {posts_per_week}
Niche: {niche}
Primary Format: {content_format}

System Analysis:
Growth Potential Index: {growth_index}
Primary Growth Lever: {primary_lever}
Expected Followers in 3 Months: {projection_mid}

Provide a structured response with:

1. Growth Diagnosis
2. Key Growth Strategy
3. Content Recommendations
4. Monetization Opportunity
5. 30 Day Action Plan
"""

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert creator growth strategist."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )

        return completion.choices[0].message.content

    except Exception as e:

        return f"AI Strategy could not be generated: {str(e)}"