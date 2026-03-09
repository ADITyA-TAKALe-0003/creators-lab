# experiment_engine.py

def generate_experiment_plan(engagement_rate, posts_per_week, content_format):

    plan = {}

    # Decide strategy type
    if engagement_rate < 3:
        strategy = "Exploration"

    elif engagement_rate < 6:
        strategy = "Optimization"

    else:
        strategy = "Reinforcement"

    # Build experiment plan

    if strategy == "Exploration":

        plan = {
            "Week 1": ["Reel", "Carousel", "Reel"],
            "Week 2": ["Carousel", "Educational Post", "Reel"],
            "Week 3": ["Storytelling Reel", "Carousel"],
            "Week 4": ["Tutorial Reel", "Carousel"]
        }

    elif strategy == "Optimization":

        plan = {
            "Week 1": [content_format, content_format, "Carousel"],
            "Week 2": [content_format, "Educational Post", content_format],
            "Week 3": [content_format, content_format],
            "Week 4": ["Carousel", content_format]
        }

    else:

        plan = {
            "Week 1": [content_format] * posts_per_week,
            "Week 2": [content_format] * posts_per_week,
            "Week 3": [content_format] * (posts_per_week + 1),
            "Week 4": [content_format] * (posts_per_week + 1)
        }

    return strategy, plan