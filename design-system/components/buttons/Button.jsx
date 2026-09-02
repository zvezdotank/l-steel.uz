import React from 'react';

export function Button({ variant = 'primary', block = false, disabled = false, icon, children, onClick }) {
  const cls = ['btn', `btn-${variant}`, block ? 'btn-block' : ''].filter(Boolean).join(' ');
  return (
    <button className={cls} disabled={disabled} onClick={onClick}>
      {children}
      {icon ? <span aria-hidden="true">{icon}</span> : null}
    </button>
  );
}
