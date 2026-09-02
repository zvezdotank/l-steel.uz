import React from 'react';

export function Card({ eyebrow, title, body, image, elevated = false, children }) {
  return (
    <div className={`card${elevated ? ' card-elev' : ''}`}>
      {image ? (
        <div className="card-media">
          <img src={image} alt="" />
        </div>
      ) : null}
      {eyebrow ? <div className="card-eyebrow">{eyebrow}</div> : null}
      {title ? <div className="card-title">{title}</div> : null}
      {body ? <div className="card-body">{body}</div> : null}
      {children}
    </div>
  );
}
