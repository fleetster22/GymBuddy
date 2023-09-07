import { LogoutHandler, Welcome } from "./Auth";

export default function Landing() {
  return (
    <div>
      <Welcome />
      <LogoutHandler />
    </div>
  );
}
