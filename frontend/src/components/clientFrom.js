import axios from "axios";
import React, { useState, useEffect } from "react";
import { v4 as uuid } from "uuid";

const ClientForm = ({ setClients, fetchData }) => {
  const [mytoken, setMytoken] = useState({ access: "" });
  const [newClient, setNewClient] = useState({
    username: "",
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
    const updatedClient = newClient;
    setNewClient(updatedClient);
    postClient(updatedClient);
  };

  const postClient = async (clientData) => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/register/",
        clientData
      );
      console.log("post data:", clientData.data);
      console.log("response data:", response.data);
      setMytoken({
        access: response.data.access,
      });
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
      <div className="token">
        <h6 className=" w-5">
          {mytoken.access
            ? mytoken.access.length > 0
              ? mytoken.access
              : "no token"
            : "waiting for token"}
        </h6>
      </div>
      <input
        type="text"
        placeholder="enter name"
        className="input input-bordered w-full max-w-xs m-4"
        value={newClient.username}
        onChange={(e) => {
          setNewClient((prev) => ({ ...prev, username: e.target.value }));
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
