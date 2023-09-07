import { LogoutHandler, Welcome } from "./Auth.js";

export default function Landing() {
  return (
    <div>
      <Welcome />
      <LogoutHandler />
    </div>
  );
}
