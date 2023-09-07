import { LogoutHandler, Welcome } from "./components/Auth";

export default function Landing() {
  return (
    <div>
      <Welcome />
      <LogoutHandler />
    </div>
  );
}
