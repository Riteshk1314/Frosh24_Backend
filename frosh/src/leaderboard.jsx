import React, { useState, useEffect } from 'react';
import './leaderboard.css';
import axios from 'axios';
import QRCode from "react-qr-code";
function Dashboard() {
  // State variables to store fetched data
  const [hoodName, setHoodName] = useState('');
  const [hoodId, setHoodId] = useState('');
  const [profilePhoto, setProfilePhoto] = useState('');
  const [qrCode, setQrCode] = useState('');
  const [secure_id, setSecure_id] = useState('');
  const [allHoods, setAllHoods] = useState([]);
  const [username, setUsername] = useState('');

  // Fetch data from /dashboard when the component mounts
  useEffect(() => {
    const fetchData = async () => {
      const token = localStorage.getItem('token');
      const storedUsername = localStorage.getItem('username');

      if (!storedUsername) {
        console.error('No username found in local storage');
        return;
      }

      setUsername(storedUsername);

      try {
        const response = await axios.post('http://127.0.0.1:8000/dashboard/', {
          registration_id: storedUsername
        }, {
          headers: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json'
          }
        });

        setHoodName(response.data.user_hood.name);
        setHoodId(response.data.user_hood.id);
        setProfilePhoto(response.data.profile_photo);
        setQrCode(response.data.qr);
        setAllHoods(response.data.all_hoods);
        setSecure_id(response.data.secure_id);
        console.log(response.data.user_hood.name );
        console.log(response.data.user_hood.id );
        console.log(response.data.profile_photo );
        console.log(response.data.qr );
        console.log(response.data.all_hoods );
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <>
      <div className="navbar-dashboard">
        <span className='frosh_logo'></span>
      </div>
      <div className='container-dashboard'>
        <img src={profilePhoto} alt="Profile" className='profile_img' />
        <div className='info'>
          <h1>USERNAME: {username}</h1>
          <h2>HOOD NAME: {hoodName}</h2>
          <h2>HOOD ID: {hoodId}</h2>
        </div>



        
        <div class ="qr_code">
  <QRCode
    size={256}
    style={{ height: "auto", maxWidth: "100%", width: "100%" }}
    value={secure_id}
    viewBox={`0 0 256 256`}
  />
</div>
      </div>
      {/* You can add a section to display all hoods if needed */}
      {/* <div className='all-hoods'>
        <h3>All Hoods:</h3>
        <ul>
          {allHoods.map(hood => (
            <li key={hood.id}>{hood.name}</li>
          ))}
        </ul>
      </div> */}
    </>
  );
}

export default Dashboard;