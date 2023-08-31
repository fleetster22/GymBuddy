import "./main.css";
import LoginForm from "./components/Login.jsx";

export default function Header() {
  return (
    <header className="header">
      <div className="header__login-button">
        <a href="./LoginForm" className="btn btn--green">
          Log in to SCULPTR
        </a>
      </div>
      <div className="header__text-box">
        <h1 className="heading-primary">
          <span className="heading-primary--main">SCULPTR</span>
          <span className="heading-primary--sub">exercise for humans</span>
        </h1>
      </div>
    </header>
  );
}
