/**
 * @startingPoint section="Components" subtitle="Primary, accent, secondary and ghost actions" viewport="700x160"
 */
export interface ButtonProps {
  /** Visual style. primary = deep blue fill, accent = safety-orange fill for CTAs like "Quote Now", secondary = outlined, ghost = text-only link-style. */
  variant?: 'primary' | 'accent' | 'secondary' | 'ghost';
  /** Stretch to fill its container. */
  block?: boolean;
  disabled?: boolean;
  /** Optional trailing icon node (Lucide icon element). */
  icon?: React.ReactNode;
  children: React.ReactNode;
  onClick?: () => void;
}
