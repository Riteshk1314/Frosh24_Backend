import React, { useState, useEffect } from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import './index.css';
import Dashboard from './leaderboard'
import Landing from './components/landing'
import Faculty from './components/faculty'
import Team from './components/team'

function App() {

  return (
    <div>
      <Routes>
        <Route exact path="/" element={ <Landing/> } />
        <Route exact path="/faculty" element={ <Faculty/> } />
        <Route exact path="/team" element={ <Team/> } />
        <Route exact path="/dashboard" element={ <Dashboard/> } />
      </Routes>


    </div>
  );
}

export default App;