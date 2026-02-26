
import { useState } from "react";
import "./App.css";
import SearchBar from "./components/searchbar";
import ContactForm from "./components/ContactCard";
import { FaPencilAlt } from "react-icons/fa";
import { useEffect } from "react";


function App() {

  const [contacts, setContacts] = useState([]);


  
  const [selectedContact, setSelectedContact] = useState(null);
  const [search, setSearch] = useState("");
  const [isModalOpen, setIsModalOpen] = useState(false);
  const fetchContacts = async () => {
  const res = await fetch("http://127.0.0.1:8000/contacts");
  const data = await res.json();
  setContacts(data);
};
useEffect(() => {
  fetchContacts();
}, []);
const saveContact = async (contactData) => {
  if (selectedContact) {
    await fetch(`http://127.0.0.1:8000/contacts/${selectedContact.id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(contactData),
    });
  } else {
    await fetch("http://127.0.0.1:8000/contacts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(contactData),
    });
  }

  fetchContacts();
  closeModal();
};
const deleteContact = async () => {
  await fetch(`http://127.0.0.1:8000/contacts/${selectedContact.id}`, {
    method: "DELETE",
  });

  fetchContacts();
  closeModal();
};



  const openAddForm = () => {
    setSelectedContact(null);
    setIsModalOpen(true);
  };

  const openEditForm = (contact) => {
    setSelectedContact(contact);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  
  

  const filteredContacts = contacts.filter(contact =>
    contact.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="app">

      <h1>Contact Book</h1>
      <p>Manage your contacts easily</p>
      <div className="top-bar">
        <SearchBar search={search} setSearch={setSearch} />
        <button className="add-btn" onClick={openAddForm}>
          + Add Contact
        </button>
      </div>

      {filteredContacts.map(contact => (
        <div key={contact.id} className="contact-row">
          <span>{contact.name}</span>
          <FaPencilAlt className="edit-icon" onClick={() => openEditForm(contact)} />
        </div>
      ))}

      {isModalOpen && (
        <div className="modal-overlay">
          <div className="modal-box">
            <ContactForm
              contact={selectedContact}
              onSave={saveContact}
              onDelete={selectedContact ? deleteContact : null}
              onClose={closeModal}
            />
          </div>
        </div>
      )}

    </div>
  );
}

export default App;
