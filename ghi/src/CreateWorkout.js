import React, { useState, useEffect } from "react";

export default function CreateWorkout() {
  const [workout, setWorkout] = useState({
    name: "",
    description: "",
    date: "",
    difficulty: "",
    type: "",
    exercises: [],
  });

  const [submission, setSubmission] = useState(false);

  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    fetch("http://localhost:3000/api/exercises")
      .then((res) => {
        if (!res.ok) {
          throw new Error(
            `Server responded with ${res.status}: ${res.statusText}`
          );
        }
        return res.json();
      })
      .then((data) => setExercises(data));
  }, []);

  function handleWorkoutChange(e) {
    setWorkout({ ...workout, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    fetch("http://localhost:3000/workouts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(workout),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then((data) => {
        console.log(data);
        setSubmission(true);
        setWorkout({
          name: "",
          description: "",
          date: "",
          difficulty: "",
          type: "",
          exercises: [],
        });
      })
      .catch((error) => {
        console.log(
          "There was a problem with the fetch operation:",
          error.message
        );
      });
  }

  if (submission) {
    return (
      <div>
        <h1>Workout Created!</h1>
        <p>Your workout has been created successfully!</p>
      </div>
    );
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
          Difficulty:
          <select
            name="difficulty"
            value={workout.difficulty}
            onChange={handleWorkoutChange}
          >
            <option value="">Difficulty</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
          </select>
        </label>
        <label>
          Exercise Type:
          <select
            name="type"
            value={workout.type}
            onChange={handleWorkoutChange}
          >
            <option value="">Exercise Type</option>
            <option value="cardio">Cardio</option>
            <option value="olympic weightlifting">Olympic Weightlifting</option>
            <option value="plyometrics">Plyometrics</option>
            <option value="powerlifting">Powerlifting</option>
            <option value="strength">Strength</option>
            <option value="stretching">Stretching</option>
            <option value="strongman">Strongman</option>
          </select>
        </label>
        <input type="submit" value="Create Workout" />
      </form>
    </div>
  );
}
