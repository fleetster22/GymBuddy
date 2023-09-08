import { useNavigate } from "react-router-dom";
import React, { useState, useEffect } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { Link } from "react-router-dom";

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
    <div>
      <button onClick={HandleLogout} className="logout-button">
        Logout
      </button>
    </div>
  );
}

export function Welcome(props) {
  const [userName, setUserName] = useState("");
  const [error, setError] = useState(null);
  const { token } = useToken();

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
          console.log("DAT2", data);
          id = data.account.id;
          console.log("ID", id);
        } else {
          throw new Error("Failed to get token user data.");
        }
      } catch (err) {
        setError(err);
      }

      if (id) {
        console.log("HERE", id);
        try {
          const userResponse = await fetch(
            `http://localhost:8000/api/accounts/detail?account_id=${id}`
          );
          if (userResponse.ok) {
            const userData = await userResponse.json();
            setUserName(userData.first_name);
            console.log("USERNAME", userName);
          } else {
            throw Error("Failed to fetch user data.");
          }
        } catch (err) {
          setError(err);
        }
      }
    };

    // Call fetchUserData here, and don't include it in the dependency array

    // Call fetchUserData here, and don't include it in the dependency array
    fetchUserData();
  }, [props.accountId]);

  return (
    <div>
      {error ? (
        <p>Error: {error.message}</p>
      ) : (
        <>
          <p>Welcome, {userName}!</p>
          <CreateWorkoutLink token={token} />{" "}
        </>
      )}
      {error ? (
        <p>Error: {error.message}</p>
      ) : (
        <>
          <p>Welcome, {userName}!</p>
          <CreateWorkoutLink token={token} />{" "}
        </>
      )}
    </div>
  );
}

export function CreateWorkoutLink({ token }) {
  if (token) {
    return (
      <li className="navigation__item">
        <Link to="../workouts/create" className="navigation__link">
          <span>Create a workout</span>
        </Link>
      </li>
    );
  } else {
    return null;
  }
}

export default Welcome;
