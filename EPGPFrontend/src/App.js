import { useState, useEffect } from "react";
import "./App.css";
import { UserTile } from "./components";

function App() {

  const [users, setUsers] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/api/users/")
      .then(response => response.json())
      .then((data) => setUsers(data))
      .catch((error) => console.error("Error fetching users:", error));
  }, []);

  return (
    <div>
      {users && users.map((user) => (
        <UserTile user={user} />
      ))}
    </div>
  );
}

export default App;