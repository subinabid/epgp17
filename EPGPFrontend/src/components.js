import React from "react";

export function UserTile({ user }) {
  return (
    <div key={user.id}>
      <h1>{user.first_name} {user.last_name}</h1>
      <p>{user.email}</p>
    </div>
  );
}