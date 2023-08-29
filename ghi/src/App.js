import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateWorkout from "./CreateWorkout.js";
// import WorkoutPage from "./WorkoutPage.jsx";
import Nav from "./Nav.js";
import AboutUs from "./About.js";
import MainPage from "./MainPage.js";

function App() {
  return (
    <BrowserRouter>
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
