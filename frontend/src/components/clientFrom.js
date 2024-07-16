import axios from "axios";
import React, { useState, useEffect } from "react";
import { v4 as uuid } from "uuid";

const ClientForm = ({ setClients, fetchData }) => {
  const [newClient, setNewClient] = useState({
    userName: "",
    // email: "",
    password: "",
    // userID: "",
  });

  const generateID = () => {
    // const newID = uuid();
    // const updatedClient = {
    //   ...newClient,
    //   userID: newID,
    // };
    const updatedClient = newClient  
    setNewClient(updatedClient);
    postClient(updatedClient);
  };

  const postClient = async (clientData) => {
    try {
      await axios.post("http://127.0.0.1:8000/register/", clientData);
      console.log("post :", clientData);
      setNewClient({
        username: "",
        // email: "",
        password: "",
        // userID: "none",
      });
      fetchData(); // Ensure fetchData is defined and works correctly
    } catch (error) {
      console.log(error.response?.data || error.message); // Log more detailed error information
    }
  };

  return (
    <div className="grid grid-flow-rol border border-black">
      <input
        type="text"
        placeholder="enter name"
        className="input input-bordered w-full max-w-xs m-4"
        value={newClient.userName}
        onChange={(e) => {
          setNewClient((prev) => ({ ...prev, userName: e.target.value }));
        }}
      />
      <input
        type="email"
        placeholder="email"
        className="input input-bordered w-full max-w-xs m-4"
        value={newClient.email}
        // onChange={(e) => {
        //   setNewClient((prev) => ({ ...prev, email: e.target.value }));
        // }}
      />
      <input
        type="password"
        placeholder="password"
        className="input input-bordered w-full max-w-xs m-4"
        value={newClient.password}
        onChange={(e) => {
          setNewClient((prev) => ({ ...prev, password: e.target.value }));
        }}
      />
      <button className="btn m-3 max-w-32 " onClick={generateID}>
        Register
      </button>
    </div>
  );
};

export default ClientForm;
