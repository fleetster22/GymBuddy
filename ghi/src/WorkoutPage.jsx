import React from "react";
import ExerciseCard from "./components/card";

export default function WorkoutPage() {
  return (
    <div className="container">
      <div>
        <h1>Your Workout Page</h1>
      </div>
      <div className="row">
        <ExerciseCard />
        <ExerciseCard />

        <div className="col-md-4">
          <p>placeholder for img</p>>
        </div>
      </div>

      <div className="row">
        <ExerciseCard />
        <ExerciseCard />
        <div className="col-md-4">
          <p>Inspirational Quote</p>
        </div>
      </div>

      <div className="row">
        <ExerciseCard />
        <ExerciseCard />
      </div>
    </div>
  );
}
