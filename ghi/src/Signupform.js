import { useState } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";
import "./main.css";

const SignupForm = () => {
  const [password, setPassword] = useState("");
  const [first, setFirst] = useState("");
  const [last, setLast] = useState("");
  const [email, setEmail] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [passwordMismatchError, setPasswordMismatchError] = useState("");

  const isValidPassword = (password) => {
    const minLength = 13;
    const hasUppercase = /[A-Z]/.test(password);
    const hasLowercase = /[a-z]/.test(password);
    const hasNumber = /\d/.test(password);
    const hasSpecialChar = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(
      password
    );

    return (
      password.length >= minLength &&
      hasUppercase &&
      hasLowercase &&
      hasNumber &&
      hasSpecialChar
    );
  };

  const { register } = useToken();
  const navigate = useNavigate();

  const handleRegistration = (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      setPasswordMismatchError("Passwords do not match.");
    }

    if (!isValidPassword(password)) {
      setPasswordError("Password does not meet the complexity requirements.");
      return;
    }

    const accountData = {
      username: email,
      password: password,
      first_name: first,
      last_name: last,
      email: email,
    };
    register(
      accountData,
      `${process.env.REACT_APP_API_HOST}/api/accounts/create`
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
              if (!isValidPassword(e.target.value)) {
                setPasswordError(
                  "Password should be at least 13 characters, have an uppercase, a lowercase, a number, and a special character."
                );
              } else {
                setPasswordError("");
              }

              if (confirmPassword && e.target.value !== confirmPassword) {
                setPasswordMismatchError("Passwords do not match.");
              } else {
                setPasswordMismatchError("");
              }
            }}
          />

          {passwordError && <div className="error">{passwordError}</div>}
          <label className="form__label">Confirm Password </label>
          <input
            name="confirmPassword"
            type="password"
            className="form__input"
            onChange={(e) => {
              setConfirmPassword(e.target.value);
              if (e.target.value !== password) {
                setPasswordMismatchError("Passwords do not match.");
              } else {
                setPasswordMismatchError("");
              }
            }}
          />

          {passwordMismatchError && (
            <div className="error">{passwordMismatchError}</div>
          )}

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
