import React, { useState, useEffect } from "react";
import { LogoutHandler, Welcome, CreateWorkoutLink } from "./Auth.js";
export default function Landing() {
  const [notCompletedWorkouts, setNotCompletedWorkouts] = useState([]);
  const [completedWorkouts, setCompletedWorkouts] = useState({
    month: 0,
    year: 0,
  });
  useEffect(() => {
    async function fetchNotCompletedWorkouts() {
      try {
        const response = await fetch(
          "http://localhost:8000/api/workouts/not-completed"
        );
        if (!response.ok) {
          throw new Error(`Failed with status: ${response.status}`);
        }
        const data = await response.json();
        if (Array.isArray(data)) {
          setNotCompletedWorkouts(data);
        } else {
          console.error("Received non-array response:", data);
        }
      } catch (error) {
        console.error("Error fetching not completed workouts:", error);
      }
    }
    async function fetchCompletedWorkouts() {
      const response = await fetch(
        "http://localhost:8000/api/completed-workouts"
      );
      const data = await response.json();
      setCompletedWorkouts(data);
    }
    fetchNotCompletedWorkouts();
    fetchCompletedWorkouts();
  }, []);
  return (
    <div>
      <Welcome />
      <LogoutHandler />

      <div className="create-workout">
        <h2 className="heading-secondary">Not Completed Workouts</h2>
        {notCompletedWorkouts.length === 0 ? (
          <p className="workout-text">No workouts pending.</p>
        ) : (
          <ul>
            {notCompletedWorkouts.map((workout) => (
              <li key={workout.id}>{workout.name}</li>
            ))}
          </ul>
        )}
        <CreateWorkoutLink />
      </div>
      <div className="create-workout">
        <h2 className="heading-secondary">Workout Stats</h2>
        <p className="workout-text">
          Completed this month: {completedWorkouts.month || 0}
        </p>
        <p className="workout-text">
          Completed this year: {completedWorkouts.year || 0}
        </p>
      </div>
    </div>
  );
}
