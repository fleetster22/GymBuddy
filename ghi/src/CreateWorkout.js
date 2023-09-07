import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function CreateWorkout() {
  const navigate = useNavigate();

  const [workout, setWorkout] = useState({
    name: "",
    description: "",
    date: "",
    difficulty: "",
    type: "",
  });
  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    const getExercises = async () => {
      try {
        let url = "http://localhost:8000/api/exercises/filter";

        if (workout.difficulty || workout.type) {
          const params = new URLSearchParams();
          if (workout.difficulty) {
            params.append("difficulty", workout.difficulty);
          }
          if (workout.type) {
            params.append("exercise_type", workout.type);
          }
          url += `?${params.toString()}`;
        }

        const exercisesResponse = await fetch(url);
        if (exercisesResponse.ok) {
          const exercisesData = await exercisesResponse.json();
          setExercises(exercisesData);
        } else {
          console.log("There was a problem with the fetch operation.");
        }
      } catch (error) {
        console.error("Failed fetching exercises:", error);
      }
    };

    getExercises();
  }, [workout]);

  function handleWorkoutChange(e) {
    setWorkout({ ...workout, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    const workout_data = {
      ...workout,
      exercises: exercises,
    };

    try {
      const response = await fetch(
        "http://localhost:8000/api/workouts/create",
        {
          method: "POST",
          body: JSON.stringify(workout_data),
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      if (response.ok) {
        navigate("/workouts");
      } else {
        console.error("Failed to submit workout.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  return (
    <div>
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
            <option value="expert">Expert</option>
          </select>
        </label>
        <label>
          Type:
          <select
            name="type"
            value={workout.type}
            onChange={handleWorkoutChange}
          >
            <option value="">Workout Type</option>
            <option value="cardio">Cardio</option>
            <option value="olympic_weightlifting">Olympic Weightlifting</option>
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
