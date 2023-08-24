import React from "react";
import Card from "Card";
import { account } from "../data";

export default function WorkoutPage() {
  return (
    <div className="container">
      <h1>{account.first_name}'s Workout Page</h1>

      <div className="row">
        <div className="col-md-4">
          <Card />
        </div>
        <div className="col-md-4">
          <Card />
        </div>
        <div className="col-md-4">
          <p>Inspirational Quote 1</p>
        </div>
      </div>

      <div className="row">
        <div className="col-md-4">
          <Card />
        </div>
        <div className="col-md-4">
          <Card />
        </div>
        <div className="col-md-4"></div>
      </div>

      <div className="row">
        <div className="col-md-4">
          <Card />
        </div>
        <div className="col-md-4">
          <Card />
        </div>
        <div className="col-md-4"></div>
      </div>
    </div>
  );
}
