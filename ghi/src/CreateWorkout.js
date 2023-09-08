import React, { useState, useEffect, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";

export default function CreateWorkout() {
  const navigate = useNavigate();
  const { token } = useAuthContext();

  const [workout, setWorkout] = useState({
    name: "",
    description: "",
    date: "",
    difficulty: "",
    type: "",
  });
  const [exercises, setExercises] = useState([]);

  const getExercises = useCallback(async () => {
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
  }, [workout.difficulty, workout.type]);

  useEffect(() => {
    if (!token) {
      navigate("/Login");
    }
  }, [navigate, token]);

  useEffect(() => {
    if (workout.difficulty || workout.type) {
      getExercises();
    }
  }, [workout.difficulty, workout.type, getExercises]);

  function handleWorkoutChange(e) {
    setWorkout({ ...workout, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    if (!token) {
      console.error("Not authorized to submit workout.");
      navigate("/Login");
      return;
    }
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
            Authorization: `Bearer ${token}`,
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
    <div className="form">
      <h1 className="form__header">Create a new Workout</h1>
      <div className="form__content">
        <form onSubmit={handleSubmit}>
          <label className="form__label">Enter a name for your workout</label>
          <input
            type="text"
            name="name"
            required
            className="form__input"
            value={workout.name}
            onChange={handleWorkoutChange}
            placeholder="Workout name"
          />

          <label className="form__label">Description</label>
          <input
            className="form__input"
            type="text"
            name="description"
            required
            placeholder="Workout description"
            value={workout.description}
            onChange={handleWorkoutChange}
          />

          <label className="form__label">Workout Date</label>
          <input
            className="form__input"
            type="date"
            name="date"
            value={workout.date}
            onChange={handleWorkoutChange}
          />

          <label className="form__label">Difficulty</label>
          <select
            className="form__input"
            name="difficulty"
            value={workout.difficulty}
            onChange={handleWorkoutChange}
          >
            <option value="">Difficulty</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="expert">Expert</option>
          </select>

          <label className="form__label">Type</label>
          <select
            className="form__input"
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
          <div className="form__button">
            <input
              className="btn btn--register"
              type="submit"
              value="Create Workout"
            />
          </div>
        </form>
      </div>
    </div>
  );
}
