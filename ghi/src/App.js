import {
  Navigate,
  useLocation,
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import { AuthProvider, useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import Nav from "./Nav.js";
import CreateWorkout from "./CreateWorkout.js";
import WorkoutPage from "./WorkoutPage.js";
import About from "./About.js";
import MainPage from "./MainPage.js";
import SignupForm from "./SignupForm.js";
import Login from "./Login.js";
import Landing from "./landing.js";

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
        </Routes>
        <Routes>
          <Route path="/MainPage" element={<MainPage />} />
          <Route path="/AboutUs" element={<AboutUs />} />
          <Route path="/SignupForm" element={<SignupForm />} />
          <Route path="/Login" element={<Login />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}
export default App;
