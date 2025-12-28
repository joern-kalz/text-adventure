interface KeyButtonProps {
    type: 'button' | 'submit';
    disabled: boolean;
    children: React.ReactNode;
    onClick?: () => Promise<void> | void;
}

export default function KeyButton({ type, disabled, children, onClick }: KeyButtonProps) {
    return (
        <button
            type={type}
            className="p-4 font-bold bg-gray-100 hover:bg-gray-200 active:bg-gray-300 text-gray-700 active:text-gray-800 border border-gray-400 active:border-gray-500 rounded-md w-20 ml-4 cursor-pointer"
            disabled={disabled}
            onClick={onClick}
        >
            {children}
        </button>
    );
}