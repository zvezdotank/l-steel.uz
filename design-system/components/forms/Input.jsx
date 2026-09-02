import React from 'react';

export function Input({ label, placeholder, type = 'text', textarea = false }) {
  return (
    <div className="field">
      {label ? <label>{label}</label> : null}
      {textarea ? (
        <textarea className="textarea" placeholder={placeholder} />
      ) : (
        <input className="input" type={type} placeholder={placeholder} />
      )}
    </div>
  );
}
