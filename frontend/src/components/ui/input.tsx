import type { InputHTMLAttributes } from "react";

export function Input(props: InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      {...props}
      style={{
        width: "100%",
        borderRadius: "0.75rem",
        border: "1px solid #cbd5e1",
        padding: "0.75rem 1rem",
        background: "rgba(255,255,255,0.9)",
        ...(props.style ?? {}),
      }}
    />
  );
}
