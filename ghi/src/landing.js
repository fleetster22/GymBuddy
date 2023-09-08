import { LogoutHandler, Welcome, CreateWorkoutLink } from "./Auth.js";

export default function Landing() {
  return (
    <div>
      <Welcome />
      <LogoutHandler />
      <CreateWorkoutLink />
    </div>
  );
}
