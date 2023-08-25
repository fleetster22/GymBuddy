import { useState, useEffect } from "react";

function ExercisesList() {
	const [exercises, setExercises] = useState([]);
	const [filterType, setFilterType] = useState("");
	const [filter, setFilter] = useState("");
	const [workout, setWorkout] = useState([]);
	const [endpoint, setEndpoint] = useState("");

	async function fetchExercises() {
		if (filterType && filter) {
			try {
				const response = await fetch(endpoint);
				if (response.ok) {
					const data = await response.json();
					setExercises(data);
				} else {
					// Handle error
					console.error("Failed to fetch exercises.");
				}
			} catch (error) {
				console.error("Error:", error);
			}
		}
	}

	const addWorkout = (entry) => {
		setWorkout([...workout, entry]);
	};

	const updateFilter = (e) => {
		setFilterType(e.target.value);
		setFilter("");
	};

	useEffect(() => {
		setEndpoint(
			`http://localhost:8000/api/exercises/${filterType ? filterType : ""}/${
				filter ? filter : ""
			}/`
		);
	}, [filter]);

	return (
		<div>
			<div>
				<select
					value={filterType}
					onChange={(e) => updateFilter(e)}
				>
					<option value="type">Types</option>
					<option value="muscle">Muscle Group</option>
					<option value="difficulty">Difficulty</option>
				</select>
				{filterType === "type" ? (
					<select
						value={filter}
						onChange={(e) => setFilter(e.target.value)}
					>
						<option value="all">All Types</option>
						<option value="cardio">Cardio</option>
						<option value="olympic_weightlifting">Olympic Weightlifting</option>
						<option value="plyometrics">Plyometrics</option>
						<option value="powerlifting">Powerlifting</option>
						<option value="strength">Strength</option>
						<option value="stretching">Stretching</option>
						<option value="strongman">Strongman</option>
					</select>
				) : filterType === "muscle" ? (
					<select
						value={filter}
						onChange={(e) => setFilter(e.target.value)}
					>
						<option value="all">All Muscles</option>
						<option value="abdominals">Abdominals</option>
						<option value="abductors">Abductors</option>
						<option value="adductors">Adductors</option>
						<option value="biceps">Biceps</option>
						<option value="calves">Calves</option>
						<option value="chest">Chest</option>
						<option value="forearms">Forearms</option>
						<option value="glutes">Glutes</option>
						<option value="hamstrings">Hamstrings</option>
						<option value="lats">Lats</option>
						<option value="lower_back">Lower Back</option>
						<option value="middle_back">Middle Back</option>
						<option value="neck">Neck</option>
						<option value="quadriceps">Quadriceps</option>
						<option value="traps">Traps</option>
						<option value="triceps">Triceps</option>
					</select>
				) : filterType === "difficulty" ? (
					<select
						value={filter}
						onChange={(e) => setFilter(e.target.value)}
					>
						<option value="all">All Difficulties</option>
						<option value="beginner">Beginner</option>
						<option value="intermediate">Intermediate</option>
						<option value="expert">Expert</option>
					</select>
				) : null}
				<button onClick={() => fetchExercises()}>Search</button>
			</div>

			<div>
				{exercises?.map((exercise) => (
					<div
						key={exercise.name}
						style={{ border: "black solid 1px", padding: "10px" }}
					>
						{workout.includes(exercise) ? (
							<h3 style={{ color: "green" }}>Added to workout</h3>
						) : null}
						<h3>{exercise.name}</h3>
						<p>{exercise.type}</p>
						<p>{exercise.muscle}</p>
						<p>{exercise.equipment}</p>
						<p>{exercise.difficulty}</p>
						<button onClick={() => addWorkout(exercise)}>Add to workout</button>
					</div>
				))}
			</div>

			<div>
				<h2>Workout</h2>
				{workout.map((exercise, index) => (
					<div key={index}>{exercise.name}</div>
				))}
			</div>
		</div>
	);
}

export default ExercisesList;
