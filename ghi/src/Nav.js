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
            <a href="./AboutUs" className="navigation__link">
              <span>About Us</span>
            </a>
          </li>
          <li className="navigation__item">
            <a href="./exercises" className="navigation__link">
              <span>Create a workout</span>
            </a>
          </li>
        </ul>
      </nav>
    </div>
  );
}
