import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Swiper, SwiperSlide } from 'swiper/react';
import SwiperCore, { EffectCoverflow, Pagination, Navigation } from 'swiper';
import 'swiper/css';
import 'swiper/css/effect-coverflow';
import 'swiper/css/pagination';
import 'swiper/css/navigation';
import './index.css';

SwiperCore.use([EffectCoverflow, Pagination, Navigation]);

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [events, setEvents] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [bookingMessage, setBookingMessage] = useState('');

  useEffect(() => {
    if (isLoggedIn) {
      fetchEvents();
    }
  }, [isLoggedIn]);

  const fetchEvents = async () => {
    setIsLoading(true);
    try {
      const response = await axios.get('http://127.0.0.1:8000/event/list');
      setEvents(response.data);
    } catch (error) {
      console.error('Error fetching events:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleUsernameChange = (e) => setUsername(e.target.value);
  const handlePasswordChange = (e) => setPassword(e.target.value);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const payload = {
      registration_id: username,
      password: password,
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/login/', payload);
      if (response.data.token) {
        setIsLoggedIn(true);
        localStorage.setItem('token', response.data.token);
      }
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  const handleBookTicket = async (eventName) => {
    const token = localStorage.getItem('token');
    if (!token) {
      console.error("No token found, user must be logged in");
      return;
    }

    const body = {
      name: eventName,
      registration_number: username
    };

    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/event/book-ticket',
        body,
        {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`
          }
        }
      );

      setBookingMessage(response.data.message);
      fetchEvents();
    } catch (error) {
      console.error("Booking failed:", error.response?.data?.error || error.message);
      setBookingMessage(error.response?.data?.error || "An error occurred while booking the ticket");
    }
  };

  return (
    <div>
      {!isLoggedIn ? (
        <div className="login">
          <div className="login-main">
            <div className="overlay">
              <div className="box">
                <form onSubmit={handleSubmit}>
                  <h4>USERNAME</h4>
                  <input
                    type="text"
                    value={username}
                    onChange={handleUsernameChange}
                    placeholder="Username"
                  />
                  <h4>PASSWORD</h4>
                  <input
                    type="password"
                    value={password}
                    onChange={handlePasswordChange}
                    placeholder="Password"
                  />
                  <button type="submit" className="log">Login</button>
                </form>
                <a href="#" className="forgot">Forgot Password?</a>
                <hr class="left"/>
                <hr class="right"/>
              </div>
            </div>
          </div>
        </div>
      ) : (
        <>
        <div className='kingbox'>
          <h1 className="heading">EVENTS</h1>
          {isLoading ? (
            <p>Loading events...</p>
          ) : events.length > 0 ? (
            <>
              {bookingMessage && <p>{bookingMessage}</p>}
              <Swiper
                effect={'coverflow'}
                grabCursor={true}
                centeredSlides={true}
                loop={true}
                slidesPerView={'auto'}
                coverflowEffect={{
                  rotate: 0,
                  stretch: 0,
                  depth: 100,
                  modifier: 2.5,
                }}
                pagination={{ el: '.swiper-pagination', clickable: true }}
                navigation={{
                  nextEl: '.swiper-button-next',
                  prevEl: '.swiper-button-prev',
                }}
                className="swiper_container"
              >
                {events.map((event, index) => (
                  <SwiperSlide key={index}>
                    <div className="slide-container">
                      {/* <img src={event.image} alt={event.name} /> */}
                      <h2 className='slide-mainheading'>{event.name}</h2>
                      <h2 className='slide-time'>{event.time}</h2>
                      <h2 className='slide-venue'>{event.venue}</h2>
                      <p className='slide-desc'>{event.description}</p>
                      {event.is_live && (
                        <button 
                          className="book-now-btn" 
                          onClick={() => handleBookTicket(event.name)}
                        >
                          Book Now
                        </button>
                      )}
                    </div>
                  </SwiperSlide>
                ))}
                <div className="swiper-pagination"></div>
                <div className="swiper-button-next"></div>
                <div className="swiper-button-prev"></div>
              </Swiper>
            </>
          ) : (
            <p>No events available.</p>
          )}
          </div>
        </>
      )}
    </div>
  );
}

export default App;