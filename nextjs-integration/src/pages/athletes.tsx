import { useState, useEffect } from "react";
import { Athlete } from "../interfaces/Athlete";

export default function AthletesPage(){
    const [athletes, setAthletes] = useState<Athlete[]>([]);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchAthletes = async() =>
        {
            try{
                const res = await fetch("/api/v1/athletes");
                if(!res.ok){
                    throw new Error("Failed to fetch athletes");
                }
                const data = await res.json();
                setAthletes(data);
            } catch (error){
                setError("Failed to fetch athletes");
            }
        };
        fetchAthletes();
    }, []);

    if(error){
        return <div>{error}</div>;
    }

    return(
        <div>
            <h1>Athletes</h1>
            <ul>
                {athletes.map((athlete) => (
                    <li key={athlete.athlete_id}>
                        {athlete.name} - {athlete.school}
                    </li>
                ))}
            </ul>
        </div>




    )
}