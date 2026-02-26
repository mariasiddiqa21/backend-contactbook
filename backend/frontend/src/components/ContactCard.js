import { useState, useEffect } from "react";

function ContactForm({ contact, onSave, onDelete, onClose }) {

  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    if (contact) {
      setName(contact.name);
      setPhone(contact.phone);
      setEmail(contact.email);
    }
  }, [contact]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave({ name, phone, email });
  };

  return (
    <form onSubmit={handleSubmit} className="form">

      <h2>{contact ? "Update Contact" : "Add Contact"}</h2>

      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Name"
        required
      />

      <input
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
        placeholder="Phone"
        required
      />

      <input
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
        required
      />

      <div className="form-buttons">
        <button type="submit">Save</button>

        {onDelete && (
          <button type="button" onClick={onDelete}>
            Delete
          </button>
        )}

        <button type="button" onClick={onClose}>
          Close
        </button>
      </div>

    </form>
  );
}

export default ContactForm;
