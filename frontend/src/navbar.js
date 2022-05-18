import "./navbar.css"
const Navbar = () => {
    return (
        <nav className="navbar">
            <h1>Food companion</h1>
            <div className="links">
                <a href="/recipes">Recipes</a>
                <a href="/plan">Plan</a>
            </div>
        </nav>
     );
}

export default Navbar;