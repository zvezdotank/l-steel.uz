window.Contact = function Contact() {
  const { Input, Button } = window.LizhongSteel;
  return (
    <div style={{padding:'64px 48px', display:'flex', gap:48, flexWrap:'wrap'}}>
      <div style={{flex:'1 1 320px', display:'flex', flexDirection:'column', gap:12}}>
        <div style={{font:'var(--text-eyebrow)', letterSpacing:'var(--letter-spacing-eyebrow)', textTransform:'uppercase', color:'var(--color-accent-600)'}}>Contact</div>
        <h1 style={{font:'var(--text-h1)'}}>Get a Quote</h1>
        <p style={{font:'var(--text-body)', color:'var(--color-text-muted)'}}>E-mail: lizhong@steelmember.com</p>
        <p style={{font:'var(--text-body)', color:'var(--color-text-muted)'}}>WhatsApp / Tel: +86-18763408501</p>
      </div>
      <div style={{flex:'1 1 320px', display:'flex', flexDirection:'column', gap:14}}>
        <Input label="Company" placeholder="Your company name" />
        <Input label="Email" type="email" placeholder="you@company.com" />
        <Input label="Message" textarea placeholder="Tell us about your project" />
        <Button variant="accent">Submit Inquiry</Button>
      </div>
    </div>
  );
};
