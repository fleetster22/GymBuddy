import { Navigate, BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider, useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import Nav from "./Nav.js";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./WorkoutPage.js";
import About from "./About.js";
import MainPage from "./MainPage.js";
import SignupForm from "./Signupform.js";
import Login from "./Login.js";
import Landing from "./landing.js";
import Footer from "./Footer.js";
import FullWorkout from "./FullWorkout.js";

const ProtectedRoute = ({ element }) => {
  const { token } = useAuthContext();
  if (!token) {
    return <Navigate to="/Login" replace />;
  }
  return element;
};
function App() {
  const baseURL = process.env.REACT_APP_API_HOST;
  return (
    <AuthProvider baseUrl={baseURL}>
      <BrowserRouter>
        <Nav />
        <Routes>
          <Route
            path="/workouts"
            element={<ProtectedRoute element={<WorkoutPage />} />}
          />
          <Route
            path="/workouts/create"
            element={<ProtectedRoute element={<CreateWorkout />} />}
          />
          <Route
            path="/landing"
            element={<ProtectedRoute element={<Landing />} />}
          />
          <Route
            path="/workouts/:workoutId"
            element={<ProtectedRoute element={<FullWorkout />} />}
          />

          <Route path="/" element={<MainPage />} />
          <Route path="/About" element={<About />} />
          <Route path="/Signupform" element={<SignupForm />} />
          <Route path="/Login" element={<Login />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </AuthProvider>
  );
}
export default App;
