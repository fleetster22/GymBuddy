import { useState, useEffect } from "react";

export default function ExerciseCard(props) {
  const [exercise, setExercise] = useState();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const getExercise = async () => {
    const exerciseUrl = "https://api.api-ninjas.com/v1/exercises";

    try {
      const exerciseResponse = await fetch(exerciseUrl, {
        headers: {
          "X-Api-Key": "g5KMn4OGpap61pP8YMZiww==WQh3U1iN7LE3M6ua",
        },
      });

      if (!exerciseResponse.ok) {
        throw new Error("Error fetching exercise data");
      }

      const exerciseData = await exerciseResponse.json();
      setExercise(exerciseData.exercise);
      setLoading(false);
    } catch (err) {
      setError(err);
      setLoading(false);
    }
  };

  useEffect(() => {
    getExercise();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading exercise: {error.message}</div>;

  return (
    <div>
      <div>
        <h2>{exercise.name}</h2>
        <p>{exercise.difficulty}</p>
        <p>{exercise.equipment}</p>
        <p>{exercise.instructions}</p>
        <button>Complete Workout</button>
      </div>
    </div>
  );
}
