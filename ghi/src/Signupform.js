import { useState } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";
import "./main.css";

const SignupForm = () => {
  const [password, setPassword] = useState("");
  const [first, setFirst] = useState("");
  const [last, setLast] = useState("");
  const [email, setEmail] = useState("");

  const { register } = useToken();
  const navigate = useNavigate();

  const handleRegistration = (e) => {
    e.preventDefault();
    const accountData = {
      username: email,
      password: password,
      first: first,
      last: last,
      email: email,
    };
    register(
      accountData,
      `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/user`
    );
    e.target.reset();
    navigate("/Login");
  };
  return (
    <div className="form">
      <h3 className="form__header">
        You're almost there! We just need a few details to get started...
      </h3>
      <div className="form__content">
        <form onSubmit={(e) => handleRegistration(e)}>
          <label className="form__label">First Name </label>
          <input
            name="first"
            type="text"
            className="form__input"
            onChange={(e) => {
              setFirst(e.target.value);
            }}
          />

          <label className="form__label">Last Name </label>
          <input
            name="last"
            type="text"
            className="form__input"
            onChange={(e) => {
              setLast(e.target.value);
            }}
          />

          <label className="form__label">Email </label>
          <input
            name="email"
            type="text"
            className="form__input"
            onChange={(e) => {
              setEmail(e.target.value);
            }}
          />

          <label className="form__label">Password </label>
          <input
            name="password"
            type="password"
            className="form__input"
            onChange={(e) => {
              setPassword(e.target.value);
            }}
          />

          <div className="form__button">
            <input
              className="btn btn--register"
              type="submit"
              value="👉  Register  👈"
            />
          </div>
        </form>
      </div>
    </div>
  );
};
export default SignupForm;
