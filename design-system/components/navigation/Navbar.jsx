import React from 'react';

export function Navbar({ active = 'HOME' }) {
  const links = ['HOME', 'ABOUT US', 'PRODUCT', 'FACTORY', 'NEWS', 'CONTACT'];
  return (
    <nav className="nav">
      <div style={{display:'flex', alignItems:'center', gap:10}}>
        <div style={{width:32, height:32, background:'var(--color-primary-600)', color:'#fff', display:'flex', alignItems:'center', justifyContent:'center', font:'700 18px var(--font-heading)'}}>W</div>
        <div style={{display:'flex', flexDirection:'column', lineHeight:1.1}}>
          <span style={{font:'700 15px var(--font-heading)', color:'var(--color-text)'}}>LIZHONG</span>
          <span style={{font:'500 9px var(--font-body)', letterSpacing:'.08em', color:'var(--color-text-muted)'}}>STEEL STRUCTURE</span>
        </div>
      </div>
      <ul className="nav-links">
        {links.map((l) => (
          <li key={l}><a href="#" className={l === active ? 'active' : ''}>{l}</a></li>
        ))}
      </ul>
    </nav>
  );
}
