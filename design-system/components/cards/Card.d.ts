/**
 * @startingPoint section="Components" subtitle="Product / news card with optional photo" viewport="700x260"
 */
export interface CardProps {
  eyebrow?: string;
  title?: string;
  body?: string;
  /** Photo URL; rendered full-bleed at the card's top edge. */
  image?: string;
  elevated?: boolean;
  children?: React.ReactNode;
}
