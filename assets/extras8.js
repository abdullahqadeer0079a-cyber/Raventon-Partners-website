import { animate, inView, hover } from "https://cdn.jsdelivr.net/npm/motion@12/+esm";

/* Scroll reveal + hover lift powered by Motion.
   - fade in + slide up 24px, once, 0.6s ease-out
   - 0.1s stagger inside grids and lists
   - hover lift scale 1.012 on cards (no bounce, no buttons)
   - disabled entirely when prefers-reduced-motion is set */

const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

const TARGETS = ".rv, .stats .grid > *, .logos";
const GROUPS = ".grid, .flow, .ind-grid, .why-cards, .checks, .timeline, .faqs, .mini-stats";
const LIFT = ".svc, .step, .quote, .post, .work, .ind, .wc, .fl";

const els = Array.from(document.querySelectorAll(TARGETS));

// take over from the CSS-only reveal
els.forEach((el) => {
  el.classList.remove("rv", "left", "right", "zoom");
  el.style.transitionDelay = "";
});

if (!reduce) {
  els.forEach((el) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(24px)";
  });

  // stagger index = position among revealed siblings inside the same group
  const indexInGroup = (el) => {
    const group = el.parentElement && el.parentElement.matches(GROUPS) ? el.parentElement : null;
    if (!group) return 0;
    return Array.from(group.children).filter((c) => els.includes(c)).indexOf(el);
  };

  els.forEach((el) => {
    const delay = Math.max(0, indexInGroup(el)) * 0.1;
    inView(
      el,
      () => {
        animate(el, { opacity: 1, y: 0 }, { duration: 0.6, ease: "easeOut", delay });
      },
      { amount: 0.15, margin: "0px 0px -40px 0px" }
    );
  });

  // hover lift (mouse only; Motion ignores touch for hover)
  hover(LIFT, (el) => {
    animate(el, { scale: 1.012 }, { duration: 0.2, ease: "easeOut" });
    return () => animate(el, { scale: 1 }, { duration: 0.2, ease: "easeOut" });
  });
} else {
  els.forEach((el) => {
    el.style.opacity = "1";
    el.style.transform = "none";
  });
}
