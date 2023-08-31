import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./WorkoutPage.jsx";
import Nav from "./Nav.js";
import About from "./About.js";
import MainPage from "./MainPage.js";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import Signupform from "./Signupform.jsx";
import Login from "./Login.jsx";
import Logout from "./Logout.jsx";
function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Nav />} />
          <Route path="/MainPage" element={<MainPage />} />
          <Route path="/AboutUs" element={<AboutUs />} />
          <Route path="/Signupform" element={<Signupform />} />
          <Route path="/Login" element={<Login />} />
          <Route path="/Logout" element={<Logout />} />
          <Route path="workouts">
            <Route index element={<WorkoutPage />} />
            <Route path="create" element={<CreateWorkout />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
