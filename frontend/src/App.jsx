import { useState } from 'react'
import './App.css'
import LiveKitModal from './components/LiveKitModal';

function App() {
  const [showSupport, setShowSupport] = useState(false);

  const handleSupportClick = () => {
    setShowSupport(true)
  }

  return (
    <div className="app">
      <header className="header">
        <div className="logo">VoiceAgent</div>
      </header>

      <main>
        <section className="hero">
          <h1>Hi I am a voice agent and my name is Nikhil Gupta</h1>
          <p>Feel free to ask any Question.</p>
          {/* <div className="search-bar">
            <input type="text" placeholder=''></input>
            <button>Search</button>
          </div> */}
        </section>

        <button className="support-button" onClick={handleSupportClick}>
          Talk to an Nikhil Gupta!
        </button>
      </main>

      {showSupport && <LiveKitModal setShowSupport={setShowSupport}/>}
    </div>
  )
}

export default App
