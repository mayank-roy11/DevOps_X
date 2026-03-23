import { useEffect, useState } from "react";

import { createFeedback, fetchFeedbacks } from "./api";

export default function App() {
  const [user_name, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  const [feedbacks, setFeedbacks] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function refresh() {
    setError("");
    setLoading(true);
    try {
      const data = await fetchFeedbacks();
      setFeedbacks(data);
    } catch (e) {
      setError(e.message || String(e));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    refresh();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function onSubmit(e) {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await createFeedback({
        user_name,
        email: email || null,
        message,
      });

      setUserName("");
      setEmail("");
      setMessage("");
      await refresh();
    } catch (e) {
      setError(e.message || String(e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container">
      <h1>Feedback System</h1>

      <form onSubmit={onSubmit} className="card">
        <label>
          Name
          <input
            value={user_name}
            onChange={(e) => setUserName(e.target.value)}
            required
            maxLength={100}
          />
        </label>

        <label>
          Email (optional)
          <input
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            type="email"
            maxLength={255}
          />
        </label>

        <label>
          Message
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            required
            minLength={5}
          />
        </label>

        <button disabled={loading} type="submit">
          {loading ? "Saving..." : "Submit feedback"}
        </button>
      </form>

      {error ? <div className="error">{error}</div> : null}

      <div className="card">
        <h2>All Feedback</h2>
        {loading ? <div>Loading...</div> : null}

        {feedbacks.length === 0 ? (
          <div>No feedback yet.</div>
        ) : (
          <ul className="list">
            {feedbacks.map((f) => (
              <li key={f.id} className="listItem">
                <div className="listTitle">{f.user_name}</div>
                <div className="listMessage">{f.message}</div>
                {f.email ? <div className="listMeta">{f.email}</div> : null}
                <div className="listMeta">
                  {new Date(f.created_at).toLocaleString()}
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

