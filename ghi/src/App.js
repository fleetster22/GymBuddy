import React, { useState, useEffect } from "react";
import { Navigate, useLocation } from "react-router-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Nav from "Nav.js";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./WorkoutPage.js";
import AboutUs from "./About.js";
import MainPage from "./MainPage.js";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import Signupform from "./Signupform.js";
import Login from "./Login.js";
import Logout from "./Logout.js";

const ProtectedRoute = ({ children }) => {
  const [token, setToken] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchToken = async () => {
      setToken(localStorage.getItem("token"));

      setLoading(false);
    };
    fetchToken();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!token) {
    return <Navigate to="/Login" replace />;
  }

  return children;
};

const UnprotectedRoute = async ({ children }) => {
  const token = localStorage.getItem("token");
  const location = useLocation();
  if (token) {
    return <Navigate to="/MainPage" replace state={{ from: location }} />;
  }
  return children;
};

function App() {
  const baseURL = process.env.REACT_APP_API_HOST;
  return (
    <AuthProvider baseUrl={baseURL}>
      <BrowserRouter>
        <Nav />
        <Routes>
          <Route element={<UnprotectedRoute />}>
            <Route path="/MainPage" element={<MainPage />} />
            <Route path="/AboutUs" element={<AboutUs />} />
            <Route path="/Signupform" element={<Signupform />} />
            <Route path="/Login" element={<Login />} />
          </Route>
          <Route element={<ProtectedRoute />}>
            <Route path="/workouts" element={<WorkoutPage />} />
            <Route path="/workouts/create" element={<CreateWorkout />} />
          </Route>
          <Route path="/landing" element={<Landing />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
