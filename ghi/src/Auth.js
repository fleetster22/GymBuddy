import { useNavigate } from "react-router-dom";
import React, { useState, useEffect } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { Link } from "react-router-dom";

export function WorkoutList({ workouts }) {
  if (!workouts) return null;
  return (
    <div className="workout-list">
      {workouts.map((workout) => (
        <div className="workout__text-box" key={workout.id}>
          <Link
            to={`/workouts/${workout.id}`}
            className="workout__text-box--link"
          >
            <h2>{workout.name}</h2>
          </Link>
          <div className="workout-list__text">
            <p>Level: {workout.difficulty}</p>
            <p>Description: {workout.description}</p>
            <p>Date:{workout.date}</p>
          </div>
        </div>
      ))}
    </div>
  );
}

export function LogoutHandler() {
  const { logout } = useToken();
  const navigate = useNavigate();
  const [token, setToken] = useState("");
  async function HandleLogout() {
    let Status = await logout();
    if (Status) {
      // Clear the token and navigate
      setToken(""); // Set the token to an empty string
      navigate("/landing");
    } else {
      console.log("Logout Fail (not logged in probably)");
    }
  }
  return (
    <div className="create-workout">
      <button onClick={HandleLogout} className="create-workout__button">
        Logout
      </button>
    </div>
  );
}
export function Welcome(props) {
  const [userName, setUserName] = useState("");
  const [error, setError] = useState(null);
  const { token } = useToken();
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    const fetchUserData = async () => {
      let id;
      try {
        const response = await fetch(`http://localhost:8000/token`, {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
          },
          credentials: "include",
        });
        if (response.ok) {
          const data = await response.json();
          id = data.account.id;
        } else {
          throw new Error("Failed to get token user data.");
        }
      } catch (err) {
        setError(err);
      }
      if (id) {
        try {
          const userResponse = await fetch(
            `http://localhost:8000/api/accounts/detail?account_id=${id}`
          );
          if (userResponse.ok) {
            const userData = await userResponse.json();
            setUserName(userData.first_name);
          } else {
            throw Error("Failed to fetch user data.");
          }
        } catch (err) {
          setError(err);
        }
      }
    };
    fetchUserData();
  }, [props.accountId, token, userName]);

  const fetchWorkouts = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/workouts");
      if (response.ok) {
        const data = await response.json();
        setWorkouts(data);
      } else {
        throw new Error("Failed to fetch workouts.");
      }
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };
  useEffect(() => {
    fetchWorkouts();
  }, []);

  return (
    <div>
      {error ? (
        <p>Error: {error.message}</p>
      ) : (
        <>
          <p className="heading-primary--sub">Welcome, {userName}!</p>
          <p>Welcome, {userName}!</p>
          <CreateWorkoutLink token={token} />
          <WorkoutList workouts={workouts} />
        </>
      )}
    </div>
  );
}
export function CreateWorkoutLink({ token }) {
  if (token) {
    return (
      <div className="create-workout">
        <Link to="../workouts/create">
          <button className="create-workout__button">Create a workout</button>
        </Link>
      </div>
    );
  } else {
    return null;
  }
}
export default Welcome;
