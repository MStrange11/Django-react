import React, { useState, useEffect } from "react";
import axios from "axios";

import "./App.css";
import Table from "./components/table";
import ClientForm from "./components/clientFrom";
import Login from "./components/login";

function App() {
  const [clients, setClients] = useState([]);
  const [isLoading, setisLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/g-stu/");
      console.log(res);
      setClients(res.data);
      setisLoading(false);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="bg-indigo-50 px-8 min-h-screen">
      <nav className="pt-8">
        <h1 className="text-5xl text-center pb-12">Connect React to Django</h1>
      </nav>
      <ClientForm setClients={setClients} fetchData={fetchData} />
      <Login />
      <Table clients={clients} setClients={setClients} isLoading={isLoading} />
    </div>
  );
}

export default App;
