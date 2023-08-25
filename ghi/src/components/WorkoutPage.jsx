import React from "react";
import ExerciseCard from "./card";

export default function WorkoutPage() {
  return (
    <div className="container">
      <h1>Your Workout Page</h1>

      <div className="row">
        <div className="col-md-4">
          <ExerciseCard />
        </div>
        <div className="col-md-4">
          <ExerciseCard />
        </div>
        <div className="col-md-4">
          <p>Inspirational Quote 1</p>
        </div>
      </div>

      <div className="row">
        <div className="col-md-4">
          <ExerciseCard />
        </div>
        <div className="col-md-4">
          <ExerciseCard />
        </div>
        <div className="col-md-4"></div>
      </div>

      <div className="row">
        <div className="col-md-4">
          <ExerciseCard />
        </div>
        <div className="col-md-4">
          <ExerciseCard />
        </div>
        <div className="col-md-4"></div>
      </div>
    </div>
  );
}
