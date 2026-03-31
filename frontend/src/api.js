const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "";
const API_PREFIX = import.meta.env.VITE_API_PREFIX || "";

export async function fetchFeedbacks() {
  const res = await fetch(`${API_BASE_URL}${API_PREFIX}/feedback/`);
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `Failed to load feedback: ${res.status}`);
  }
  return res.json();
}

export async function createFeedback({ user_name, email, message }) {
  const res = await fetch(`${API_BASE_URL}${API_PREFIX}/feedback/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_name, email, message }),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `Failed to create feedback: ${res.status}`);
  }
  return res.json();
}