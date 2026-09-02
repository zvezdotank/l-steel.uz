window.Home = function Home() {
  const { Button, Card } = window.LizhongSteel;
  const categories = [
    ['Conventional Steel...', 'primary'], ['Public Curtain Wall', 'primary'],
    ['Steel Components', 'primary'], ['Hot Rolled Finished...', 'accent'],
  ];
  return (
    <div>
      <div style={{height:220, background:'linear-gradient(135deg,var(--color-primary-700),var(--color-primary-500))', display:'flex', alignItems:'center', padding:'0 48px'}}>
        <div>
          <div style={{font:'var(--text-h2)', color:'#fff'}}>Lizhong Steel Structure/Production and Processing</div>
          <div style={{font:'var(--text-body)', color:'var(--color-primary-100)', marginTop:8}}>All varieties, specifications, materials, resources, tailor-made, fast delivery, and after-sales service.</div>
        </div>
      </div>

      <div style={{display:'grid', gridTemplateColumns:'repeat(4,1fr)', gap:2, background:'var(--color-border)'}}>
        {categories.map(([label, v]) => (
          <button key={label} className={`btn btn-${v}`} style={{borderRadius:0, padding:'14px 8px'}}>{label}</button>
        ))}
      </div>

      <section style={{padding:'56px 48px', display:'flex', flexDirection:'column', gap:24}}>
        <div className="section-heading">
          <div className="label">Hot Products</div>
          <svg className="chevron" width="20" height="12" viewBox="0 0 20 12" fill="none" stroke="currentColor" strokeWidth="2"><path d="M2 2l8 8 8-8"/></svg>
        </div>
        <div style={{display:'grid', gridTemplateColumns:'repeat(3,1fr)', gap:20}}>
          <Card title="Steel Structure Factory Building" body="Light steel frame system built from H-, Z- and U-shaped steel components." />
          <Card title="Steel Structure Stadium" body="High-quality steel shaped to almost any span, seating hundreds to thousands." />
          <Card title="Curtain Wall Structural Parts" body="T-shaped, triangular and square/rectangular tube profiles." />
        </div>
      </section>

      <section style={{padding:'0 48px 56px', display:'flex', flexDirection:'column', gap:16, alignItems:'center', textAlign:'center'}}>
        <div className="section-heading">
          <div className="label">About Us</div>
          <svg className="chevron" width="20" height="12" viewBox="0 0 20 12" fill="none" stroke="currentColor" strokeWidth="2"><path d="M2 2l8 8 8-8"/></svg>
        </div>
        <p style={{font:'var(--text-body)', color:'var(--color-text-muted)', maxWidth:640}}>Lizhong Steel Structure (Shandong) Co., Ltd., located in Jinan Laiwu District, is a set design, manufacturing, construction integrated service provider in the field of steel structure. It has independent import and export rights, and its products are sold all over the world.</p>
      </section>
    </div>
  );
};
