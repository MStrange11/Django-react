import React, { useState } from "react";
import axios from "axios";

import { v4 as uuid } from "uuid";
import {
  MdOutlineDeleteOutline,
  MdEditNote,
  MdOutlineCheckBox,
  MdOutlineCheckBoxOutlineBlank,
} from "react-icons/md";

const Table = ({ clients, setClients, isLoading }) => {
  const [editText, setEditText] = useState({
    userName: "",
  });

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/clients/${id}/`);
      const newList = clients.filter((client) => client.id !== id);
      setClients(newList);
    } catch (error) {
      console.log(error);
    }
  };

  const handleEdit = async (id, value) => {
    try {
      const response = await axios.patch(
        `http://127.0.0.1:8000/api/clients/${id}/`,
        value
      );
      console.log(response.data);
      const newClient = clients.map((client) =>
        client.id === id ? response.data : client
      );
      setClients(newClient);
    } catch (error) {
      console.log(error);
    }
  };

  const handleClick = () => {
    handleEdit(editText.id, editText);
    // console.log(editText.id, editText);
    setEditText({
      userName: "",
    });
  };

  const handleCheckbox = (id, value) => {
    handleEdit(id, {
      userID: uuid(),
    });
  };

  return (
    <div className="py-16">
      <table className="w-11/12 max-w-4xl">
        <thead className="border-b-2 border-black">
          <tr>
            <th className="p-3 text-sm font-semibold tracking-wide text-left">
              checkbox
            </th>
            <th className="p-3 text-sm font-semibold tracking-wide text-left">
              username
            </th>
            <th className="p-3 text-sm font-semibold tracking-wide text-left">
              email
            </th>
            <th className="p-3 text-sm font-semibold tracking-wide text-left">
              userID
            </th>
            <th className="p-3 text-sm font-semibold tracking-wide text-left">
              Action
            </th>
          </tr>
        </thead>
        <tbody>
          {isLoading ? (
            <div>Is Loading</div>
          ) : (
            <>
              {clients.map((client, i) => {
                return (
                  <tr key={client.id} className="border-b border-black">
                    <td className="p-3 text-sm" title={client.id}>
                      <span className="inline-block cursor-pointer">
                        <MdOutlineCheckBox onClick={()=>handleCheckbox(client.id)}/>
                      </span>
                    </td>
                    <td className="p-3 text-sm">{client.userName}</td>
                    <td className="p-3 text-sm">{client.email}</td>
                    <td className="p-3 text-sm">{client.userID}</td>
                    <td className="p-3 text-sm font-medium grid grid-flow-col items-center mt-5">
                      <span>
                        <label htmlFor="my-modal">
                          <MdEditNote
                            onClick={() => setEditText(client)}
                            className=" text-xl cursor-pointer"
                          />
                        </label>
                      </span>
                      <span className="inline-block cursor-pointer">
                        <MdOutlineDeleteOutline
                          onClick={() => handleDelete(client.id)}
                        />
                      </span>
                    </td>
                  </tr>
                );
              })}
            </>
          )}
        </tbody>
      </table>
      {/* Modal */}
      <input type="checkbox" id="my-modal" className="modal-toggle" />
      <div className="modal">
        <div className="modal-box">
          <h3 className="font-bold text-lg">Edit Todo</h3>
          <input
            type="text"
            value={editText.userName}
            onChange={(e) => {
              setEditText((prev) => ({
                ...prev,
                userName: e.target.value,
              }));
            }}
            placeholder="Type here"
            className="input input-bordered w-full mt-8"
          />
          <input
            type="text"
            value={editText.email}
            placeholder="Type here"
            className="input input-bordered w-full mt-8"
            readOnly
            style={{ pointerEvents: "none" }}
          />
          <div className="modal-action">
            <label
              htmlFor="my-modal"
              onClick={handleClick}
              className="btn btn-primary"
            >
              Edit
            </label>
            <label htmlFor="my-modal" className="btn">
              Close
            </label>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Table;
