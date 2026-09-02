window.About = function About() {
  const { Tag } = window.LizhongSteel;
  return (
    <div style={{padding:'64px 48px', display:'flex', flexDirection:'column', gap:20, maxWidth:760}}>
      <h1 style={{font:'var(--text-h1)'}}>Lizhong Steel Structure (Shandong) Co., Ltd.</h1>
      <svg width="20" height="12" viewBox="0 0 20 12" fill="none" stroke="var(--color-primary-500)" strokeWidth="2"><path d="M2 2l8 8 8-8"/></svg>
      <p style={{font:'var(--text-body-lg)', color:'var(--color-text-muted)'}}>Located in Jinan Laiwu District, Lizhong Steel Structure is a set design, manufacturing and construction integrated service provider in the field of steel structure. It is the advocate and promoter of China's construction industrialization, and a contract-abiding, credit-heavy enterprise with independent import and export rights — its products are sold worldwide.</p>
      <div style={{display:'flex', gap:10, flexWrap:'wrap'}}>
        <Tag variant="outline">ISO 9001</Tag>
        <Tag variant="outline">ISO 45001</Tag>
        <Tag variant="outline">ISO 14001</Tag>
      </div>
      <hr className="hr" />
      <div style={{font:'var(--text-h3)'}}>Team</div>
      <p style={{font:'var(--text-body)', color:'var(--color-text-muted)'}}>2 professional construction engineers, 6 senior managers, 15 international and domestic marketing and service personnel, and more than 90 professional manufacturing personnel.</p>
    </div>
  );
};
