export default function Navbar() {
    return (
        <nav className="navbar is-justify-content-space-between">
            <div className="">
                Cookbook
            </div>
            <div className="is-flex is-flex-direction-row">
                <button className="navbar-item button is-primary">log in</button>
                <button className="navbar-item button is-secondary">Register</button>
            </div>
        </nav>
    )
}