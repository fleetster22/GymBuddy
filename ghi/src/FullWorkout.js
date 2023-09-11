import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export function FullWorkout() {
  const { workoutId } = useParams();
  const [workout, setWorkout] = useState(null);

  useEffect(() => {
    const fetchWorkout = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/api/workouts/${workoutId}`
        );
        if (response.ok) {
          const data = await response.json();
          setWorkout(data);
        } else {
          throw new Error("Failed to fetch workout details.");
        }
      } catch (err) {}
    };
    // below only run the ID if the workout exists, because it is looking for the ID when it runs the useeffect
    workoutId && fetchWorkout();
  }, []);

  if (!workout) {
    return null;
  }

  return (
    <div>
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
  );
}
export default FullWorkout;
