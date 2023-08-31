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
      <Routes>
        <Nav />
        <Route path="/MainPage" element={<MainPage />} />
        <Route path="/AboutUs" element={<AboutUs />} />
        <Route path="workouts">
          <Route index element={<WorkoutPage />} />
          <Route path="create" element={<CreateWorkout />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
