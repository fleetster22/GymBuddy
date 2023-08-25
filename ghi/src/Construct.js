import React from "react";

function Construct(props) {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Sculptr App</h1>
        <h2>Under construction</h2>
        <h2>Coming on (or before)</h2>
        <h2>
          Module: {props.info.module} Week: {props.info.week} Day:{" "}
          {props.info.day}
        </h2>
        <h2>
          by or <strong>WELL BEFORE</strong> {props.info.hour}:{props.info.min}{" "}
          Cohort Time
        </h2>
      </header>
    </div>
  );
}

export default Construct;
