import type { HTMLAttributes, PropsWithChildren } from "react";

export function ScrollArea({ children, style, ...props }: PropsWithChildren<HTMLAttributes<HTMLDivElement>>) {
  return (
    <div
      {...props}
      style={{
        overflowY: "auto",
        background: "rgba(255,255,255,0.6)",
        backdropFilter: "blur(8px)",
        ...(style ?? {}),
      }}
    >
      {children}
    </div>
  );
}
