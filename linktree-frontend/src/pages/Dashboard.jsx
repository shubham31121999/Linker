import { useState } from "react";
import API from "../api";

export default function Dashboard() {
  const [description, setDescription] = useState("");
  const [links, setLinks] = useState([{ title: "", url: "" }]);

  // ✅ Get token from localStorage (saved during login)
  const token = localStorage.getItem("token");

  const handleAddLink = () => {
    if (links.length < 6) setLinks([...links, { title: "", url: "" }]);
  };

  const handleChange = (index, field, value) => {
    const updated = [...links];
    updated[index][field] = value;
    setLinks(updated);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // ✅ Send to the correct backend route + include token in header
      const res = await API.post(
        "/dashboard/",
        { description, links },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      alert("✅ Profile saved successfully!");
      console.log(res.data);
    } catch (err) {
      console.error("❌ Error saving dashboard:", err);
      alert("Failed to save dashboard. Check console for details.");
    }
  };

  return (
    <div className="container">
      <h2>Your Dashboard</h2>
      <textarea
        placeholder="Your description..."
        onChange={(e) => setDescription(e.target.value)}
      />

      {links.map((link, i) => (
        <div key={i}>
          <input
            placeholder="Title"
            value={link.title}
            onChange={(e) => handleChange(i, "title", e.target.value)}
          />
          <input
            placeholder="URL"
            value={link.url}
            onChange={(e) => handleChange(i, "url", e.target.value)}
          />
        </div>
      ))}

      <button onClick={handleAddLink}>Add another link</button>
      <button onClick={handleSubmit}>Save</button>
    </div>
  );
}
