import "./main.css";
import { Link } from "react-router-dom";

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
            <Link
              to="/MainPage"
              reloadDocument={true}
              className="navigation__link"
            >
              <span>Home</span>
            </Link>
          </li>
          <li className="navigation__item">
            <Link
              to="/About"
              reloadDocument={true}
              className="navigation__link"
            >
              <span>About Us</span>
            </Link>
          </li>
          <li className="navigation__item">
            <Link
              to="/SignupForm"
              reloadDocument={true}
              className="navigation__link"
            >
              <span>Sign Up</span>
            </Link>
          </li>
          <li className="navigation__item">
            <Link
              to="/Login"
              reloadDocument={true}
              className="navigation__link"
            >
              <span>Login</span>
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}
