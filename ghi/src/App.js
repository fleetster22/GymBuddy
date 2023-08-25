import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./components/WorkoutPage.jsx";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="workouts" element={<WorkoutPage />} />
        <Route path="workouts/new" element={<CreateWorkout />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
