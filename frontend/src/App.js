import './App.css';
import Recipes from './recipes';
import Navbar from './navbar';

const Data = ["Ranajky", "Desiaita", "Polievka", "Obed", "Olovrant", "Vecera"];

function App() {
    return (
        <div className="App">
            <Navbar />
            <div className="content">
                <Recipes />
            </div>
        </div>
    );
}

export default App;
