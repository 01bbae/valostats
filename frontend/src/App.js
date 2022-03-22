import React from "react";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import Home from "./components/Home";
import AuthSuccess from "./components/Auth";
import AuthFailed from "./components/AuthFailed";
import ErrorPage from "./components/ErrorPage";


function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/auth" element={<AuthSuccess />} />
          <Route path="/authfailed" element={<AuthFailed />} />
          <Route path="*" element={<ErrorPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
