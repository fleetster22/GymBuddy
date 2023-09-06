import React, { useState, useEffect } from "react";

export default function WorkoutPage() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/workouts");
        if (response.ok) {
          const data = await response.json();
          setWorkouts(data);
        } else {
          throw new Error("Failed to fetch workouts.");
        }
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading workout: {error.message}</div>;

  return (
    <div>
      <h1>Your Workouts</h1>
      <div className="row">
        {workouts.map((workout) => (
          <div className="col-md-4" key={workout.id}>
            <h2>{workout.name}</h2>
            <p>{workout.difficulty}</p>
            <p>{workout.description}</p>
            <p>{workout.date}</p>
            <div>
              {workout.exercises.map((exercise, index) => (
                <div key={index}>
                  <p>Exercise Name: {exercise.name}</p>
                  <p>Exercise Type: {exercise.type}</p>
                  <p>Targeted Muscle Group:{exercise.muscle}</p>
                  <p>Equipment: {exercise.equipment}</p>
                  <p>Difficulty: {exercise.difficulty}</p>
                  <p>Instructions: {exercise.instructions}</p>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
