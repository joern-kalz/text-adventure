export default function LoadingSpinner() {
    return (
        <div className="absolute top-0 left-0 w-full h-full flex items-center justify-center">
            <div className="h-5 w-5 animate-spin rounded-full border-2 border-solid border-black border-t-transparent"></div>
        </div>
    );
}