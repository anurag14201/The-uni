import { Parallax } from 'react-parallax';
import './App.css';
import hire from "../src/img/pexels-johannes-plenio-1114900.jpg"

function App() {
  return (
    <div>
      <Parallax className="lg:w-full md:w-32" strength={-800} bgImage={hire}>
        <header>

        </header>
      </Parallax>

    </div>
  );
}

export default App;
