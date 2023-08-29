import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./WorkoutPage.jsx";
// import WorkoutPage from "./WorkoutPage.jsx";
import Nav from "./Nav.js";
import AboutUs from "./About.js";
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
      <div>
        <Nav />

        <Routes>
          <Route path="exercises">
            <Route index element={<CreateWorkout />} />
            {/* <Route path="history" element={<WorkoutPage />} /> */}
          </Route>
          <Route path="/MainPage" element={<MainPage />} />
          <Route path="/AboutUs" element={<AboutUs />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
