import React from "react";

// import Swiper core and required modules


import { Swiper, SwiperSlide } from 'swiper/react';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/effect-coverflow';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

import { EffectCoverflow, Pagination, Navigation } from 'swiper/modules';

// import { EffectCoverflow, pagination} from 'swiper' ;

import img1 from '../assets/images/img_1.png'
import img2 from '../assets/images/img_2.png'
import img3 from '../assets/images/img_3.png'
import img4 from '../assets/images/img_4.png'
import img5 from '../assets/images/img_5.png'

const Events = ()=>{
    return (
        <div className="container-events">
             <h1 className="heading-events">Events</h1>
             <Swiper
             effect = {'coverflow'}
             grabCursor = {true}
             centeresSlides = {true}
             slidesPreview = {'auto'}
             coverflowEffect = {
                {
                    rotate:0,
                    stretch: 0,
                    depth: 100,
                    modifier: 2.5,
                }
             }
             pagination={{el: '', clickable:true}}
             navigation = { {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
                clickable: true,
             }}
             modules = {[EffectCoverflow, Pagination, Navigation]}
             className='swiper_container'
             >
                <SwiperSlide>
                    <img src={img1} alt="img1" />
                </SwiperSlide>
                <SwiperSlide>
                    <img src={img2} alt="img1" />
                </SwiperSlide>
                <SwiperSlide>
                    <img src={img3} alt="img1" />
                </SwiperSlide>
                <SwiperSlide>
                    <img src={img4} alt="img1" />
                </SwiperSlide>

                <div className="slider-controler">
                    <div className="swiper-button-prev slider-arrow">
                        <ion-icon name="arrow-back-outline"  ></ion-icon>
                    </div>
                    <div className="swiper-button-next slider-arrow">
                        <ion-icon name="arrow-forward-outline"  ></ion-icon>
                    </div>
                    <div className="swiper-pagination">

                    </div>
                </div>

             </Swiper>
        </div>
    )
}

export default Events
