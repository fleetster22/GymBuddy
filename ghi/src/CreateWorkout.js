import React, { useState, useEffect } from "react";

export default function CreateWorkout() {
  const [workout, setWorkout] = useState({
    name: "",
    description: "",
    date: "",
    exercises: [],
  });

  const [exercises, setExercises] = useState([]);

  const [textarea, setTextarea] = useState("");

  useEffect(() => {
    fetch("http://localhost:3000/api/exercises")
      .then((res) => res.json())
      .then((data) => setExercises(data));
  }, []);

  function handleWorkoutChange(e) {
    setWorkout({ ...workout, [e.target.name]: e.target.value });
  }

  function handleExerciseChange(e) {
    const exercise = exercises.find((ex) => ex.id === parseInt(e.target.value));
    setWorkout({
      ...workout,
      exercises: [...workout.exercises, exercise],
    });
  }

  function handleSubmit(e) {
    e.preventDefault();
    fetch("http://localhost:3000/api/workouts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(workout),
    })
      .then((res) => res.json())
      .then((data) => console.log(data));
  }

  return (
    <div className="container">
      <h1>Create Workout</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Enter a name for your workout
          <input
            type="text"
            name="name"
            required
            value={workout.name}
            onChange={handleWorkoutChange}
            placeholder="Workout name"
          />
        </label>
        <label>
          Description:
          <input
            type="text"
            name="description"
            required
            placeholder="Workout description"
            value={workout.description}
            onChange={handleWorkoutChange}
          />
        </label>
        <label>
          Workout Date:
          <input
            type="date"
            name="date"
            value={workout.date}
            onChange={handleWorkoutChange}
          />
        </label>
        <label>
          Exercises:
          <select onChange={handleExerciseChange}>
            <option value="">Exercise Types</option>
            {exercises.map((ex) => (
              <option key={ex.name} value={ex.name}>
                {ex.name}
              </option>
            ))}
          </select>
        </label>
        <input type="submit" value="Create Workout" />
      </form>
    </div>
  );
}
