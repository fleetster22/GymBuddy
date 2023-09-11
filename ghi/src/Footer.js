import React from "react";
import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer__logo-box">
        <img src="../Sculptr.png" alt="Sculptr logo" className="footer__logo" />
        <h2 className="heading-primary--main">SCULPTR</h2>
        <h3 className="heading-primary--sub">Development Team</h3>
      </div>
      <div className="row">
        <div className="col-1-of-3">
          <p className="footer__content">
            <h4>Background</h4> This application was created by a team of
            developers as a learning project. This took place during the Hack
            Reactor by Galvanize 19 week intensive software engineering
            bootcamp.
          </p>
        </div>
        <div className="col-1-of-3">
          <p className="footer__content">
            <h4>Our Journey</h4> We started this project with a team of five
            developers but as the weeks wore on our numbers dwindled down to
            three. Through coordination and perserverence we were able to
            accomplish our goal.
          </p>
        </div>
        <div className="col-1-of-3">
          <div className="footer__content">
            <h4>The Developers</h4>
            <p>
              <Link
                to="https://www.linkedin.com/in/priya-patel-ms2/"
                className="footer__link"
              >
                Priya Patel
              </Link>
            </p>
            <p>
              <Link
                to="https://www.linkedin.com/in/anaka-norfleet/"
                className="footer__link"
              >
                Anaka Norfleet
              </Link>
            </p>
            <p>
              <Link
                to="https://www.linkedin.com/in/michaeljamesparnapy/"
                className="footer__link"
              >
                Michael Parnapy
              </Link>
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}
