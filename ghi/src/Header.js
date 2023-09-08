import "./main.css";

export default function Header() {
  return (
    <header className="header">
      <div className="header__login-button">
        <a href="./Login" className="header__login-button--text">
          user login
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
