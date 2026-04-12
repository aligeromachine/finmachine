export const CodeBlock = ({ content }) => {
    return (
        <pre
            style={{
                whiteSpace: 'pre-wrap', // Preserve line breaks and wrap text
                wordBreak: 'break-word', // Break long words if needed
                overflowWrap: 'break-word', // Alternative to word-break
                fontFamily: 'monospace', // Use monospace font for code
                backgroundColor: '#f5f5f5', // Light gray background
                padding: '1rem', // Add some padding
                borderRadius: '4px', // Optional rounded corners
                maxWidth: '100%', // Ensure it doesn't overflow container
                overflowX: 'auto', // Add horizontal scroll if needed
                color: '#e03c3c',
            }}
        >
            {content}
        </pre>
    );
};
