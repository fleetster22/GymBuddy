import { useState, useEffect } from "react";

function ExercisesList() {
	const [exercises, setExercises] = useState([]);
	const [filters, setFilters] = useState({
		type: "all",
		muscle: "all",
		difficulty: "all",
	});
	const [workout, setWorkout] = useState([]);
}

async function fetchExercises() {
	let endpoint = "/";

	if (filters.type !== "all") endpoint = `/type/${filters.type}`;
	else if (filters.muscle !== "all") endpoint = `/muscle/${filters.muscle}`;
	else if (filters.difficulty !== "all")
		endpoint = `/difficulty/${filters.difficulty}`;

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
return (
	<div>
		<div>
			<select
				value={filters.type}
				onChange={(e) =>
					setFilters((prev) => ({ ...prev, type: e.target.value }))
				}
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

			<select
				value={filters.muscle}
				onChange={(e) =>
					setFilters((prev) => ({ ...prev, muscle: e.target.value }))
				}
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

			<select
				value={filters.difficulty}
				onChange={(e) =>
					setFilters((prev) => ({ ...prev, difficulty: e.target.value }))
				}
			>
				<option value="all">All Difficulties</option>
				<option value="beginner">Beginner</option>
				<option value="intermediate">Intermediate</option>
				<option value="expert">Expert</option>
			</select>

			<button onClick={fetchExercises}>Search</button>
		</div>

		<div>
			{exercises.map((exercise) => (
				<div key={exercise.name}>
					<h3>{exercise.name}</h3>
					<p>{exercise.type}</p>
					<p>{exercise.muscle}</p>
					<p>{exercise.equipment}</p>
					<p>{exercise.difficulty}</p>
					<button onClick={() => setWorkout((prev) => [...prev, exercise])}>
						Add to workout
					</button>
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

export default ExercisesList;
