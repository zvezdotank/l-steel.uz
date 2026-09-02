import React from 'react';

const ICONS = {
  inquiry: <path d="M4 4h16v12H8l-4 4V4z" />,
  whatsapp: <path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.7-1.2A9 9 0 1 0 12 3z" />,
  email: <path d="M4 5h16v14H4z M4 5l8 7 8-7" />,
  top: <path d="M12 5l-7 7h4v7h6v-7h4z" />,
};

export function StickyToolbar({ items = ['inquiry', 'whatsapp', 'email', 'top'] }) {
  const labels = { inquiry: 'Inquiry', whatsapp: 'Whatsapp', email: 'Email', top: 'Top' };
  return (
    <div className="toolbar">
      {items.map((key) => (
        <div key={key} className="toolbar-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6">{ICONS[key]}</svg>
          {labels[key]}
        </div>
      ))}
    </div>
  );
}
