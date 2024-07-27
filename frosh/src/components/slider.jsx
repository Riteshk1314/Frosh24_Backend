import React, { useState } from "react";
import SliderBg from '../assets/images/img_2.png'



export default (props) => {
  const [activeSlide, setactiveSlide] = useState(props.activeSlide);

  const next = () =>
    activeSlide < props.events.length - 1 && setactiveSlide(activeSlide + 1);

  const prev = () => activeSlide > 0 && setactiveSlide(activeSlide - 1);

  const getStyles = (index) => {
    if (activeSlide === index)
      return {
        opacity: 1,
        transform: "translateX(0px) translateZ(0px)",
        zIndex: 10
      };
    else if (activeSlide - 1 === index)
      return {
        opacity: 1,
        transform: "translateX(-240px) translateZ(-400px)",
        zIndex: 9
      };
    else if (activeSlide + 1 === index)
      return {
        opacity: 1,
        transform: "translateX(240px) translateZ(-400px) ",
        zIndex: 9
      };
    else if (activeSlide - 2 === index)
      return {
        opacity: 1,
        transform: "translateX(-480px) translateZ(-500px)",
        zIndex: 8
      };
    else if (activeSlide + 2 === index)
      return {
        opacity: 1,
        transform: "translateX(480px) translateZ(-500px) ",
        zIndex: 8
      };
    else if (index < activeSlide - 2)
      return {
        opacity: 0,
        transform: "translateX(-480px) translateZ(-500px) ",
        zIndex: 7
      };
    else if (index > activeSlide + 2)
      return {
        opacity: 0,
        transform: "translateX(480px) translateZ(-500px) ",
        zIndex: 7
      };
  };

  return (
    <div className="bg-slider">
      {/* carousel */}
      <div className="slideC">
        {props.events.map((event, index) => (
          <React.Fragment key={index}>
            <div
              className="slide"
              style={{
                background: `url(${SliderBg})`,
                boxShadow: `0 5px 20px ${SliderBg}30`,
                ...getStyles(index)
              }}
            >
              <SliderContent {...event} handleBookTicket={props.handleBookTicket} bookingMessage={props.bookingMessage} />
            </div>
          </React.Fragment>
        ))}
      </div>
      {/* carousel */}

      <div className="btns">
        <div className="btn"
          onClick={prev}
          color="#fff">
          <img width="50" height="50" src="https://img.icons8.com/ios-glyphs/30/FFFFFF/left.png" alt="left"/>
        </div>

        <div className="btn"
          onClick={next}
          color="#fff">
          <img width="50" height="50" src="https://img.icons8.com/ios-glyphs/30/FFFFFF/arrow.png" alt="arrow"/>
        </div>
      </div>
    </div>
  );
};

const SliderContent = (props) => {
  return (
    <div className="sliderContent">
      <div className="sliderContentHead">

        <h2>{props.name}</h2>
      </div>
      <div className="sliderContentInfo">
        <p><img style={{color: "white"}} width="24" height="24" src="https://img.icons8.com/material-sharp/24/clock.png" alt="clock"/> {props.time}</p>
        <p><img style={{color: "white"}} width="24" height="24" src="https://img.icons8.com/material-rounded/24/marker.png" alt="marker"/>  {props.venue}</p>
        <p><img style={{color: "white"}} width="24" height="24" src="https://img.icons8.com/fluency-systems-regular/48/calendar--v1.png" alt="calendar--v1"/> {props.description}</p>

      </div>
            <div className="book-now">
              <button className="book-now-btn" onClick={() => props.handleBookTicket(props.name)}>
                  BOOK NOW
              </button>

            </div>
      {/* {(props.is_live && props.bookingMessage!="Ticket booked successfully" ) && (
        )} */}
    </div>
  );
};
