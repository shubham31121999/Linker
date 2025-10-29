import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="home">
      <h1>Linkify 🌐</h1>
      <p>Create your personal link page — one link for everything you do.</p>

      <div className="actions">
        <Link to="/signup" className="btn">Sign Up</Link>
        <Link to="/login" className="btn-outline">Login</Link>
      </div>
    </div>
  );
}
