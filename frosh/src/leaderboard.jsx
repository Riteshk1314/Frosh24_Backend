import React, { useState, useEffect } from 'react';
import './leaderboard.css';

function Dashboard() {
  // State variables to store fetched data
  const [name, setName] = useState('');
  const [regId, setRegId] = useState('');
  const [hood, setHood] = useState('');
  const [qrCodeImage, setQrCodeImage] = useState('');
  const [dp, setDp] = useState('');

  // Fetch data from /users when the component mounts
  useEffect(() => {
    fetch('http://127.0.0.1:8000/users')
      .then(response => response.json())
      .then(data => {
        setName(data.name);
        setRegId(data.registration_id);
        setHood(data.hood);
        setQrCodeImage(data.qr_code_image);
        setDp(data.image);
      })
      .catch(error => console.error('Error fetching user data:', error));
  }, []);

  return (
    <>
      <div className="navbar">
        <span className='frosh_logo'></span>
      </div>
      <div className='container'>
        <img src={dp} alt="Profile" className='profile_img' />
        <div className='info'>
          <h1>NAME: {name}</h1>
          <h2>APPLICATION NUMBER: {regId}</h2>
          <h2>HOOD: {hood}</h2>
        </div>
        <img src={qrCodeImage} alt="QR Code" className='qr_code' />
      </div>
    </>
  );
}

export default Dashboard;