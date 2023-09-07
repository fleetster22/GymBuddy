import "./main.css";

export default function Nav() {
  return (
    <div className="navigation">
      <input
        type="checkbox"
        className="navigation__checkbox"
        id="navi-toggle"
      />
      <label htmlFor="navi-toggle" className="navigation__button">
        <span className="navigation_icon">&nbsp;</span>
        <p className="navigation__button--text">MENU</p>
      </label>

      <div className="navigation__background">&nbsp;</div>

      <nav className="navigation__nav">
        <ul className="navigation__list">
          <li className="navigation__item">
            <a href="/MainPage" className="navigation__link">
              <span>Home</span>
            </a>
          </li>
          <li className="navigation__item">
            <a href="./About" className="navigation__link">
              <span>About Us</span>
            </a>
          </li>
          <li className="navigation__item">
            <a href="./CreateWorkout" className="navigation__link">
              <span>Create a workout</span>
            </a>
          </li>
          <li className="navigation__item">
            <a href="./Signupform" className="navigation__link">
              <span>Sign Up</span>
            </a>
          </li>
          <li className="navigation__item">
            <a href="./Login" className="navigation__link">
              <span>Login</span>
            </a>
          </li>
          <li className="navigation__item">
            <a href="./Logout" className="navigation__link">
              <span>Logout</span>
            </a>
          </li>
        </ul>
      </nav>
    </div>
  );
}
