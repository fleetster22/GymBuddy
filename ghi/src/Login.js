import useToken from "@galvanize-inc/jwtdown-for-react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useToken();
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    login(username, password);
    e.target.reset();
    navigate("/landing");
  };

  return (
    <div className="form">
      <h3 className="form__header">Login to begin your workout</h3>
      <div className="form__content">
        <form onSubmit={(e) => handleSubmit(e)}>
          <label className="form__label">Your email address</label>
          <input
            name="username"
            type="text"
            required
            className="form__input"
            onChange={(e) => setUsername(e.target.value)}
          />

          <label className="form__label">Password</label>
          <input
            name="password"
            type="password"
            required
            className="form__input"
            onChange={(e) => setPassword(e.target.value)}
          />

          <div className="form__button">
            <input
              className="btn btn--register"
              type="submit"
              value="👉  Login  👈"
            />
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
