import React, { useState, useEffect } from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import './index.css';
import './media.css'
// import Login from './components/login'
import Dashboard from './leaderboard'
import Landing from './components/landing'
import Faculty from './components/faculty'
import Team from './components/team'
import Events from './components/events';
import Slider from './components/slider'
import data from './components/data'
import './slide.css'
import Navigate from './components/navigate'
import ScrollToTop from './components/scrollToTop';





function App() {

  return (
    <div>
      <ScrollToTop/>
      <Routes>
        <Route exact path="/" element={ <Landing/> } />
        <Route exact path="/faculty" element={ <Faculty/> } />
        <Route exact path="/team" element={ <Team/> } />
        <Route exact path="/dashboard" element={ <Dashboard/> } />
        <Route exact path='/events' element={ <Events/> } />
        <Route exact path='/slider' element={ <Slider events={data} activeSlide={2}  /> } />
        <Route exact path = "/map" element={<> <Navigate /></>}/>
      </Routes>


    </div>
  );
}

export default App;