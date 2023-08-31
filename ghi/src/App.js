import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./WorkoutPage.jsx";
import MainPage from "./MainPage.js";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="workouts">
          <Route index element={<WorkoutPage />} />
          <Route path="create" element={<CreateWorkout />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
