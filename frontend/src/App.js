import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ShelfChef from "./components/ShelfChef";
import { Toaster } from "./components/ui/toaster";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<ShelfChef />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;