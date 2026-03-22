type SourcePanelProps = {
  sources: { file_path: string; text: string }[];
};

export function SourcePanel({ sources }: SourcePanelProps) {
  return (
    <div className="source-panel">
      {sources.map((source, index) => (
        <div className="source-item" key={`${source.file_path}-${index}`}>
          <div className="source-path">{source.file_path}</div>
          <pre className="source-code">{source.text}</pre>
        </div>
      ))}
    </div>
  );
}
