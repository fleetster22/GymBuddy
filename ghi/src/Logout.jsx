import React from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";

import { useNavigate } from "react-router-dom";

function LogoutHandler() {
  const { logout } = useToken();
  const navigate = useNavigate();

  async function HandleLogout() {
    let Status = await logout();
    if (Status) {
      navigate("/");
    }
    // Logout fails
    else {
      console.log("Logout Fail (not logged in probably)");
    }
  }

  return { HandleLogout };
}

function LogoutButton() {
  const { HandleLogout } = LogoutHandler();

  return (
    <button onClick={HandleLogout} className="logout-button">
      Logout
    </button>
  );
}

export default LogoutButton;
