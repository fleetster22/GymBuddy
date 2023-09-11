import FullWorkout from "./FullWorkout.js";
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
      <div className="landing-container">
        <div className="workouts-section">
          <h2>Not Completed Workouts</h2>
          {notCompletedWorkouts.length === 0 ? (
            <p>No workouts pending.</p>
          ) : (
            <ul>
              {notCompletedWorkouts.map((workout) => (
                <li key={workout.id}>{workout.name}</li>
              ))}
            </ul>
          )}
          <CreateWorkoutLink />
        </div>
        <div className="stats-section">
          <h2>Workout Stats</h2>
          <p>Completed this month: {completedWorkouts.month || 0}</p>
          <p>Completed this year: {completedWorkouts.year || 0}</p>
        </div>
        <FullWorkout />
      </div>
    </div>
  );
}
