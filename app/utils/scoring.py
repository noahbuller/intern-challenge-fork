import os
import json

# Grab the scoring json file from the config dir
SCORING_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../../config/scoring_config.json")
print(SCORING_CONFIG_PATH)
# Function to get the scoring config file
def load_scoring_config():
    with open(SCORING_CONFIG_PATH, "r") as f:
        scoring_config = json.load(f)
    return scoring_config

#Variable used in scoring function below
SCORING_CONFIG = load_scoring_config()

def calculate_scoring_weights(athletic_performance, social_media, brand_compatability):
    scoring_weights= SCORING_CONFIG["weights"]

    total_score = (
        (athletic_performance * scoring_weights["athletic_performance"]) +
        (social_media * scoring_weights["social_media"]) +
        (brand_compatability * scoring_weights["brand_compatability"])
    )

    return total_score

# Function based on how social media factors affect score
def calculate_social_media_factors(followers, engagement_rate,content_quality):
    social_media_weights = SCORING_CONFIG["social_media_weights"]

    total_score = (
        (followers * social_media_weights["followers"]) +
        (engagement_rate * social_media_weights["engagement_rate"]) +
        (content_quality * social_media_weights["content_quality"])
    )

    return total_score

# Function based on how performance factors affect score
def calculate_performance_factors(recent_results, improvement_trend, competition_level):
    performance_weights = SCORING_CONFIG["performance_results"]

    total_score = (
        (recent_results * performance_weights["recent_results"]) +
        (improvement_trend * performance_weights["improvement_trend"]) +
        (competition_level * performance_weights["competition_level"])
    )

    return total_score

#Function based on brand compatability affects score
def calculate_brand_compatability_factors(sports_relevance, audience_alignment, brand_values_match):
    brand_compatability_weights = SCORING_CONFIG["brand_compatability_weights"]
    
    total_score = (
        (sports_relevance * brand_compatability_weights["sports_relevance"]) +
        (audience_alignment * brand_compatability_weights["audience_alignment"]) +
        (brand_values_match * brand_compatability_weights["brand_values_match"])
    )

    return total_score

