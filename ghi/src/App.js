import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./WorkoutPage.jsx";
import Nav from "./Nav.js";
import About from "./About.js";
import MainPage from "./MainPage.js";

// import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";

function App() {
  return (
    <BrowserRouter>
      <Nav />
      <Routes>
        <Route path="/MainPage" element={<MainPage />} />
        <Route path="/About" element={<About />} />
        <Route path="workouts">
          <Route index element={<WorkoutPage />} />
          <Route path="create" element={<CreateWorkout />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
