import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./WorkoutPage.jsx";
import Nav from "./Nav.js";
import AboutUs from "./About.js";
import MainPage from "./MainPage.js";

function App() {
  return (
    <BrowserRouter>
      <Nav />
      <Routes>
        <Route path="/MainPage" element={<MainPage />} />
        <Route path="/AboutUs" element={<AboutUs />} />
        <Route path="/workouts" element={<WorkoutPage />} />
        <Route path="/workouts/create" element={<CreateWorkout />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
