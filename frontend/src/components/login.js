import React, { useState } from "react";
import axios from "axios";

const Login = () => {
  const [username, setUsername] = useState("utsav@gmail.com");
  const [password, setPassword] = useState("12345");
  const [error, setError] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/login/", { username, password });
      // const response = await axios.post("http://127.0.0.1:8000/api/token/", { "mohit", "451236" });
      console.log("Login successful:", response.data);
      // Redirect or handle successful login here
    } catch (error) {
      console.error("Login error:", error.response);
      setError("Invalid credentials. Please try again.");
    }
  };

  return (
    <div className="grid grid-flow-rol border border-black">
      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <input
            type="text"
            value={username}
            placeholder="username"
            className="input input-bordered w-full max-w-xs m-4"
            onChange={(e) => setUsername(e.target.value)}
            // required
          />
        </div>
        <div>
          <input
            type="password"
            value={password}
            placeholder="Password"
            className="input input-bordered w-full max-w-xs m-4"
            onChange={(e) => setPassword(e.target.value)}
            // required
          />
        </div>
        <button type="submit" className="btn m-3 max-w-32 ">
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
