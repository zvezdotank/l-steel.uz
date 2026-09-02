import React from 'react';

export function Tag({ variant = 'neutral', children }) {
  return <span className={`tag tag-${variant}`}>{children}</span>;
}
