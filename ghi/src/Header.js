import "./main.css";

export default function Header() {
  return (
    <header className="header">
      <div className="header__login-button">
        <a href="./Login" className="header__login-button--text">
          user login
        </a>
      </div>
      <br />
      <div className="header__signup-button">
        <a href="./Signupform" className="header__signup-button--text">
          sign up
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
