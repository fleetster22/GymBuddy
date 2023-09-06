import React, { useState, useEffect } from "react";

export default function WorkoutPage() {
  const [workouts, setWorkouts] = useState([]);
  const [userName, setUserName] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const userResponse = await fetch("http://localhost:8000/api/accounts");
        if (userResponse.ok) {
          const data = await userResponse.json();
          setUserName(data.first_name);
        } else {
          throw new Error("Failed to fetch user data.");
        }
      } catch (err) {
        setError(err);
      }
    };

    fetchUserData();
  }, []);

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
      <h1>{userName}'s Workout Page</h1>
      <div className="row">
        {workouts.map((workout) => (
          <div className="col-md-4" key={workout.id}>
            <h2>{workout.name}</h2>
            <p>{workout.difficulty}</p>
            <p>{workout.description}</p>
            <p>{workout.date}</p>
            <p>{workout.exercises}</p>
            <button>Complete Workout</button>
          </div>
        ))}
      </div>
    </div>
  );
}
