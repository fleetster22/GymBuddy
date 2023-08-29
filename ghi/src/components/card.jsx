import { useState, useEffect } from "react";

export default function ExerciseCard(props) {
  const [exercises, setExercises] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getExercises = async () => {
      const API_KEY = process.env.API_KEY;
      const API_BASE_URL = process.env.API_BASE_URL;
      try {
        const exerciseResponse = await fetch(API_BASE_URL, {
          headers: {
            "X-Api-Key": API_KEY,
          },
        });

        if (!exerciseResponse.ok) {
          throw new Error("Error fetching exercise data");
        }

        const exerciseData = await exerciseResponse.json();
        setExercises(exerciseData);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    getExercises();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading exercise: {error.message}</div>;

  return (
    <div className="row">
      {exercises.map((exercise) => (
        <div className="col-md-4" key={exercise.id}>
          {" "}
          <h2>{exercise.name}</h2>
          <p>{exercise.difficulty}</p>
          <p>{exercise.equipment}</p>
          <p>{exercise.instructions}</p>
          <button>Complete Workout</button>
        </div>
      ))}
    </div>
  );
}
