import {
  LogoutHandler,
  Welcome,
  CreateWorkoutLink,
  WorkoutList,
} from "./Auth.js";
import FullWorkout from "./FullWorkout.js";

export default function Landing() {
  return (
    <div>
      <Welcome />
      <LogoutHandler />
      <CreateWorkoutLink />
      <WorkoutList />
      <FullWorkout />
    </div>
  );
}
