export interface Athlete{
    athlete_id: number;
    name: string;
    school: string;
    year?: string;
    score?: number;
}

export interface AthleteIG{
    id: string;
    handle: string;
    followers?: number;
    posts?: number;
    is_private?: boolean;
    fetch_time?: string;
    social_score?: number;
}

export interface AthleteMedia{
    athlete_id: string;
    headshot_url?: string;
}   

export interface Score{
    score_id: number;
    athlete_id: number;
    season: number;
    score: number;
    created_at: string;
    updated_at: string;
}

export interface Brand{
    brand_id: number;
    name: string;
    logo_url?: string;
    website_url?: string;
    create_at?: string;
    updated_at?: string;
}

export interface SignedAthlete{
    id: number;
    athlete_id: number;
    brand_id: number;
    signed_date?: string;
    contract_details?: any; //should be JSON
}

export interface WatchlistAthlete{
    athlete_id: string;
    brand_id: string;
    added_date?: string;
    notes?: any; //should be JSON
}

export interface ScoringWeights {
    athletic_performance: number;
    social_media: number;
    brand_compatibility: number;
}

export interface SocialMediaFactors {
    followers: number;
    engagement_rate: number;
    content_quality: number;
}

export interface PerformanceFactors {
    recent_results: number;
    improvement_trend: number;
    competition_level: number;
}

export interface BrandCompatibilityFactors {
    sport_relevance: number;
    audience_alignment: number;
    brand_values_match: number;
}

export interface ScoringConfig {
    scoring_weights: ScoringWeights;
    social_media_factors: SocialMediaFactors;
    performance_factors: PerformanceFactors;
    brand_compatibility_factors: BrandCompatibilityFactors;
    follower_thresholds: {
        low: number;
        medium: number;
        high: number;
        very_high: number;
    };
    engagement_rate_thresholds: {
        low: number;
        medium: number;
        high: number;
        very_high: number;
    };
    performance_improvement_thresholds: {
        low: number;
        medium: number;
        high: number;
        very_high: number;
    };
}