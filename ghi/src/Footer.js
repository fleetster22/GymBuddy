import React from "react";
import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer__logo-box">
        <img
          src="../GymBuddy.png"
          alt="GymBuddy logo"
          className="footer__logo"
        />
        <h2 className="heading-primary--main">GymBuddy</h2>
        <h3 className="heading-primary--sub">Development</h3>
      </div>
      <div className="row">
        <div className="col-1-of-3">
          <div className="footer__content">
            <h4>Background</h4>
            <p>
              The GymBuddy application was created as a final project for the
              Hack Reactor by Galvanize 19 week intensive software engineering
              bootcamp from May to September 2023.
            </p>
          </div>
        </div>
        <div className="col-1-of-3">
          <div className="footer__content">
            <h4>My Journey</h4>
            <p>
              When deciding on a final project, I wanted to create something
              that I would myself. Drawing from my own passion in fitness was a
              no-brainer for my first full-stack application.
            </p>
          </div>
        </div>
        <div className="col-1-of-3">
          <div className="footer__content">
            <h4>The Developer</h4>
            <p>
              <img
                src="../linkedin_icon.png"
                alt="LinkedIn Logo"
                className="footer__icon"
              />
              <Link
                to="https://www.linkedin.com/in/anaka-norfleet/"
                className="footer__link"
              >
                Anaka Norfleet
              </Link>
              <br />
              <img
                src="../tacohackr_favicon.png"
                alt="TacoHackr Logo"
                className="footer__icon"
              />
              <Link to="https://www.tacohackr.app" className="footer__link">
                Website
              </Link>
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}
