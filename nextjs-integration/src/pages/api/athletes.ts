import { NextApiRequest, NextApiResponse } from 'next';
import { Athlete, ScoringWeights } from '../../interfaces/Athlete';

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse<Athlete[] | { error: string }>
) {
    try {
        // Fetch all athletes from the FastAPI 
        const athletesResponse = await fetch('http://localhost:8000/api/v1/athletes');
        if (!athletesResponse.ok) {
            throw new Error('Failed to fetch athletes');
        }
        const athletes: Athlete[] = await athletesResponse.json();

        // Fetch weighted scores for each athlete from FASTAPI
        const athletesWithScores = await Promise.all(
            athletes.map(async (athlete) => {
                const scoringWeightsResponse = await fetch(
                    `http://localhost:8000/api/v1/athletes/${athlete.athlete_id}/scoring_weights`
                );
                if (!scoringWeightsResponse.ok) {
                    throw new Error(`Failed to fetch scoring weights for athlete ${athlete.athlete_id}`);
                }
                const scoringWeights: ScoringWeights = await scoringWeightsResponse.json();

                // Fetch age for each athlete
                const ageResponse = await fetch(
                    `http://localhost:8000/api/v1/athletes/${athlete.athlete_id}/age`
                );
                if (!ageResponse.ok) {
                    throw new Error(`Failed to fetch age for athlete ${athlete.athlete_id}`);
                }
                const ageData = await ageResponse.json();

                
            })
        );

    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to fetch athletes' });
    }
}