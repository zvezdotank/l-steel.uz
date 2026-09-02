window.Products = function Products() {
  const { Card, StickyToolbar } = window.LizhongSteel;
  const products = [
    ['Steel Structure Garage', 'Steel structure garages provide compact, multi-level parking.'],
    ['Steel Structure Factory Building', 'Steel structure factory building is a new type of light steel structure building.'],
    ['Steel Structure Stadium', 'Steel-structured arenas are made of high-quality steel, built to almost any shape.'],
    ['Steel Structure Warehouse', 'A new type of light steel structure building system.'],
    ['Steel Structure Bridge', 'Steel bridges use steel as the main construction material.'],
    ['Curtain Wall Structural Parts', 'T-shaped, triangular and square/rectangular tube profiles.'],
  ];
  return (
    <div>
      <div style={{padding:'12px 48px', color:'var(--color-text-muted)', font:'var(--text-body-sm)', background:'var(--color-bg-alt)'}}>Home page &gt; Products</div>
      <div style={{padding:'0 48px'}}>
        <div style={{background:'var(--color-primary-500)', color:'#fff', textAlign:'center', padding:'14px', font:'600 15px var(--font-body)'}}>All categories</div>
      </div>
      <div style={{padding:'32px 48px', display:'grid', gridTemplateColumns:'repeat(3,1fr)', gap:20}}>
        {products.map(([title, body]) => <Card key={title} title={title} body={body} />)}
      </div>
      <StickyToolbar />
      <div style={{padding:'24px 48px', display:'flex', justifyContent:'center', gap:8, font:'var(--text-body-sm)', color:'var(--color-text-muted)'}}>
        {[1,2,3,4].map((n) => (
          <div key={n} style={{width:28, height:28, display:'flex', alignItems:'center', justifyContent:'center',
            background: n===1 ? 'var(--color-primary-500)' : 'transparent', color: n===1 ? '#fff' : 'var(--color-text-muted)'}}>{n}</div>
        ))}
        <div>… 25</div>
      </div>
    </div>
  );
};
