import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./WorkoutPage.jsx";

function App() {
  return (
    <BrowserRouter>
      <div>
        <Routes>
          <Route path="exercises">
            <Route index element={<CreateWorkout />} />
            <Route path="history" element={<WorkoutPage />} />
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
