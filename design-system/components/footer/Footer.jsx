import React from 'react';

export function Footer() {
  return (
    <footer className="footer">
      <div style={{display:'flex', gap:48, flexWrap:'wrap', paddingBottom:32}}>
        <div style={{flex:'2 1 260px'}}>
          <h3>CONTACT US</h3>
          <p style={{font:'var(--text-body-sm)'}}>E-mail: lizhong@steelmember.com</p>
          <p style={{font:'var(--text-body-sm)'}}>Whatsapp / Tel: +86-18763408501</p>
          <div style={{display:'flex', gap:12, marginTop:16}}>
            <div className="footer-qr">Whatsapp QR</div>
            <div className="footer-qr">WeChat QR</div>
          </div>
          <div style={{display:'flex', gap:10, marginTop:16}}>
            {['f','ig','yt','tt'].map((s) => (
              <div key={s} className="footer-social">{s}</div>
            ))}
          </div>
        </div>
        <div style={{flex:'1 1 200px'}}>
          <h3>PRODUCTS</h3>
          <ul className="footer-list">
            <li>Conventional Steel Structure Building</li>
            <li>Public Steel Structure Building</li>
            <li>Steel Components</li>
            <li>Glass Curtain Wall Exquisite Steel</li>
            <li>Hot Rolled Finished Profiles</li>
          </ul>
        </div>
      </div>
      <div className="footer-bottom">Copyright © Lizhong Steel Structure (Shandong) Co., Ltd. · 鲁ICP备2023046018号-1 · Business license</div>
    </footer>
  );
}
