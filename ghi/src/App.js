import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateWorkout from "./components/CreateWorkout.js";
// import WorkoutPage from "./components/WorkoutPage.jsx";

function App() {
	return (
		<BrowserRouter>
			<div>
				<Routes>
					<Route path="/">
						<Route
							index
							element={<CreateWorkout />}
						/>
						{/* <Route
							path="history"
							element={<WorkoutPage />} */}
						{/* /> */}
					</Route>
				</Routes>
			</div>
		</BrowserRouter>
	);
}

export default App;
