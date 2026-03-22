import type { ButtonHTMLAttributes, PropsWithChildren } from "react";

type ButtonProps = PropsWithChildren<ButtonHTMLAttributes<HTMLButtonElement>>;

export function Button({ children, style, ...props }: ButtonProps) {
  return (
    <button
      {...props}
      style={{
        border: "none",
        borderRadius: "0.75rem",
        padding: "0.75rem 1rem",
        background: props.disabled ? "#94a3b8" : "#0f766e",
        color: "#fff",
        cursor: props.disabled ? "not-allowed" : "pointer",
        ...style,
      }}
    >
      {children}
    </button>
  );
}
