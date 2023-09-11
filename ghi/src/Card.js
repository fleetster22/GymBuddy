import "./main.css";
import { Link } from "react-router-dom";

export default function Card() {
  return (
    <div className="row">
      <div className="col-1-of-3">
        <div className="card">
          <div className="card__side card__side--front">
            <div className="card__picture card__picture--1">&nbsp;</div>
            <h4 className="card__heading">
              <span className="card__heading-span card__heading-span--1">
                Beginner program
              </span>
            </h4>
            <div className="card__details">
              <ul>
                <li>Improve fitness</li>
                <li>Lose weight</li>
                <li>Guided workouts</li>
                <li>Exercise stats</li>
                <li>Difficulty: easy</li>
              </ul>
            </div>
          </div>
          <div className="card__side card__side--back card__side--back-1">
            <div className="card__cta">
              <div className="card__price-box">
                <p className="card__price-only"></p>
                <p className="card__price-value">Start training today!</p>
              </div>
              <div className="about-button">
                <Link to="/SignupForm" className="about-button__click">
                  Sign me up!
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="col-1-of-3">
        <div className="card">
          <div className="card__side card__side--front">
            <div className="card__picture card__picture--2">&nbsp;</div>
            <h4 className="card__heading">
              <span className="card__heading-span card__heading-span--2">
                intermediate program
              </span>
            </h4>
            <div className="card__details">
              <ul>
                <li>Muscle specific</li>
                <li>Body type specific</li>
                <li>Create workouts</li>
                <li>Save workouts</li>
                <li>Difficulty: medium</li>
              </ul>
            </div>
          </div>
          <div className="card__side card__side--back card__side--back-2">
            <div className="card__cta">
              <div className="card__price-box">
                <p className="card__price-only"></p>
                <p className="card__price-value">A new you is waiting</p>
              </div>
              <div className="about-button">
                <Link to="./SignupForm" className="about-button__click">
                  Create my login
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="col-1-of-3">
        <div className="card">
          <div className="card__side card__side--front">
            <div className="card__picture card__picture--3">&nbsp;</div>
            <h4 className="card__heading">
              <span className="card__heading-span card__heading-span--3">
                Advanced program
              </span>
            </h4>
            <div className="card__details">
              <ul>
                <li>Choose exercises</li>
                <li>Create workout</li>
                <li>Track your progress</li>
                <li>Earn badges!</li>
                <li>Difficulty: hard</li>
              </ul>
            </div>
          </div>
          <div className="card__side card__side--back card__side--back-3">
            <div className="card__cta">
              <div className="card__price-box">
                <p className="card__price-only"></p>
                <p className="card__price-value">Get sculpted today</p>
              </div>
              <div className="about-button">
                <Link to="./SignupForm" className="about-button__click">
                  I want to get fit
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
