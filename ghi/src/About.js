import React from "react";

export default function About() {
  return (
    <div className="about">
      <h1 className="about__heading--main">About Us</h1>
      <ul className="detail">
        <li className="description">
          Welcome to Sculptr, the ultimate fitness app that empowers you to
          craft your dream physique by selecting and exploring exercises
          tailored to your preferred difficulty level. At Sculptr, we're
          dedicated to revolutionizing your fitness journey, offering a unique
          platform that puts you in control of sculpting your body.
        </li>
        <h2 className="about__heading--sub">Our Mission</h2>
        <li className="description__secondary">
          Our mission at Sculptr is to provide individuals with a dynamic and
          personalized fitness experience. We understand that everyone's fitness
          goals and starting points are different. That's why we've developed an
          app that lets you choose and explore exercises based on your desired
          level of challenge. Whether you're a seasoned fitness enthusiast or
          just starting your wellness journey, Sculptr is here to guide you
          every step of the way.
        </li>
        <h2 className="about__heading--sub">How It Works</h2>
        <li className="description__secondary">
          Sculptr makes achieving your fitness aspirations a breeze. Here's how
          it works: 1. Choose Your Difficulty: Begin by selecting your preferred
          difficulty level. Whether you're looking for a gentle start or a more
          intense challenge, Sculptr has exercises suited to your needs. 2.
          Explore Exercises: Browse our extensive library of exercises
          specifically categorized by difficulty. With detailed instructions and
          visuals, you can explore each exercise to understand its form and
          benefits. 3. Curate Your Workouts: Create your very own personalized
          workouts by combining exercises that align with your fitness goals.
          Mix and match to design a routine that's perfect for you. 4. Track
          Your Progress: Monitor your progress and achievements as you conquer
          exercises and complete workouts. Sculptr provides you with insights
          into your journey, helping you stay motivated.
        </li>
        <li className="description__tertiary">
          Download Sculptr today and embark on a new era of personalized fitness
          exploration.
        </li>

        <li className="description__tertiary">
          Shape Your Body. Shape Your Future. Shape Your Way with Sculptr.
        </li>
        <div className="about-button">
          <a href="./SignupForm" className="about-button__click">
            🎆 Sign Up Today! 🎆
          </a>
        </div>
      </ul>
    </div>
  );
}
