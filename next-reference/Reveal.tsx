"use client";

import { motion, useReducedMotion, type HTMLMotionProps } from "motion/react";
import type { ReactNode } from "react";

/**
 * Reusable scroll reveal: fades in and slides up 24px when it enters the
 * viewport (once only, 0.6s, ease-out). Respects prefers-reduced-motion.
 *
 * Next.js App Router: install with `npm i motion`, then import from any
 * server or client component.
 */
type RevealProps = Omit<HTMLMotionProps<"div">, "initial" | "whileInView" | "viewport"> & {
  children: ReactNode;
  /** extra delay in seconds (use RevealGroup for automatic staggering) */
  delay?: number;
  /** lift to scale 1.03 on hover (cards, buttons) */
  lift?: boolean;
};

export function Reveal({ children, delay = 0, lift = false, ...rest }: RevealProps) {
  const reduce = useReducedMotion();

  if (reduce) {
    return <div {...(rest as object)}>{children}</div>;
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 24 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.15 }}
      transition={{ duration: 0.6, ease: "easeOut", delay }}
      whileHover={lift ? { scale: 1.03 } : undefined}
      {...rest}
    >
      {children}
    </motion.div>
  );
}

/**
 * Staggers its direct children by 0.1s (grids and lists).
 * Usage: <RevealGroup className="grid"> <Card/> <Card/> </RevealGroup>
 */
export function RevealGroup({
  children,
  className,
  stagger = 0.1,
}: {
  children: ReactNode[] | ReactNode;
  className?: string;
  stagger?: number;
}) {
  const items = Array.isArray(children) ? children : [children];
  return (
    <div className={className}>
      {items.map((child, i) => (
        <Reveal key={i} delay={i * stagger}>
          {child}
        </Reveal>
      ))}
    </div>
  );
}
