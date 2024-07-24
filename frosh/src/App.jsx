import React, { useState, useEffect } from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import axios from 'axios';
import { Swiper, SwiperSlide } from 'swiper/react';
import SwiperCore, { EffectCoverflow, Pagination, Navigation } from 'swiper';
import 'swiper/css';
import 'swiper/css/effect-coverflow';
import 'swiper/css/pagination';
import 'swiper/css/navigation';
import './index.css';
import Nav from './components/nav'
import Home from './components/Home'
import Map from './components/Map'
import Desc from './components/Desc'
import Login from './components/login'
import Dashboard from './leaderboard'
import Landing from './components/landing'
import Faculty from './components/faculty'
import Team from './components/team'


SwiperCore.use([EffectCoverflow, Pagination, Navigation]);

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