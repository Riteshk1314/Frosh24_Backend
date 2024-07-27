import React, { useState, useEffect } from "react";
import axios from 'axios';
import Slider from './slider';
import Home from './Home';
import Nav from './nav';
import Map from './Map';
import Desc from './Desc';
import Login from './Signin';

const Landing = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [events, setEvents] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [bookingMessage, setBookingMessage] = useState('');

    useEffect(() => {
        // Retrieve username from local storage
        const savedUsername = localStorage.getItem('username');
        if (savedUsername) {
            setUsername(savedUsername);
        }
    }, []);

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
                // Save username in local storage
                localStorage.setItem('username', username);
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
        <>  
            <Nav isLoggedIn={isLoggedIn}/>
            <Home/>
            {!isLoggedIn ? (
                <Login 
                    handlePasswordChange={handlePasswordChange} 
                    handleSubmit={handleSubmit} 
                    handleUsernameChange={handleUsernameChange} 
                    username={username} // Pass the username to the Login component for pre-filling
                />
            ) : (
                <>
                    <div className='kingbox'>
                        {isLoading ? (
                            <p>Loading events...</p>
                        ) : events.length > 0 ? (
                            <>
                                {bookingMessage && <p>{bookingMessage}</p>}
                                <Slider events={events} activeSlide={2} handleBookTicket={handleBookTicket} bookingMessage={bookingMessage} />
                            </>
                        ) : (
                            <p>No events available.</p>
                        )}
                    </div>
                </>
            )}
            <Map/>
            <Desc/>
        </>
    );
}

export default Landing;