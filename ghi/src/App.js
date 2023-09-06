import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./WorkoutPage.js";
import Nav from "./Nav.js";
import AboutUs from "./About.js";
import MainPage from "./MainPage.js";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import Signupform from "./Signupform.js";
import Login from "./Login.js";
import Logout from "./Logout.js";
function App() {
  const baseURL = process.env.REACT_APP_API_HOST;
  return (
    <AuthProvider baseUrl={baseURL}>
      <BrowserRouter>
        <Nav />

        <Routes>
          <Route path="/MainPage" element={<MainPage />} />
          <Route path="/AboutUs" element={<AboutUs />} />
          <Route path="/Signupform" element={<Signupform />} />
          <Route path="/Login" element={<Login />} />
          <Route path="/Logout" element={<Logout />} />
          <Route path="/workouts" element={<WorkoutPage />} />
          <Route path="/workouts/create" element={<CreateWorkout />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
