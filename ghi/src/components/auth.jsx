import React from "react";
import { useNavigate } from "react-router-dom";

import React, { useEffect, useState } from "react";

function Welcome(props) {
  return <h1>Welcome, {props.name}</h1>;
}

----

function LogoutHandler() {
  const { logout } = useToken();
  const navigate = useNavigate();

  async function HandleLogout() {
    let Status = await logout();
    if (Status) {
      navigate("/");
    } else {
      console.log("Logout Fail (not logged in probably)");
    }
  }

  return { HandleLogout };
}

function Welcome(props) {
  return <h1>Welcome, {props.name}</h1>;
}

function LogoutButton() {
  const { HandleLogout } = LogoutHandler();

  return (
    <div>
      <Welcome name="John" /> {/* Replace "John" with the user's actual name */}
      <button onClick={HandleLogout} className="logout-button">
        Logout
      </button>
    </div>
  );
}

export default LogoutButton;

function App() {
  return (
    <div>
      {/* Pass the 'name' property from the user's profile to the Welcome component */}
      <Welcome name={userProfile.name} />
    </div>
  );
}

export default App;
