import React from 'react'
import {Link} from 'react-router-dom'
import Triangle from '../assets/images/triangle.png'

const OurTeam = () => {
    return (
        <div className='bg-desc' id='about'>
            <div className="frosh-alpha">
                <div className="three">
                    <div className="one" >F</div>   
                    <div className="two" >
                        <div className="desc-head">
                            FAMILY
                        </div>
                        <p>Frosh aims to build a sense of faith amongst the three pillars holding the institute together with the faculty, the seniors, and the freshers.</p>
                    </div>
                </div>
                <div className="three">
                    <div className="one">R</div>   
                    <div className="two" >
                        <div className="desc-head">
                            RELIABLE
                        </div>

                        <p>Frosh provides a reliable support system to hold hands through times that one might face.</p>
                    </div>

                </div >
                <div className="three">
            
                    <div className="one" >O</div>   
                    <div className="two">
                        <div className="desc-head">
                            OPTIMISTIC
                            
                        </div>


                        <p>Frosh believes in an optimistic approach while dealing with the challenges one has to face in life.</p>
                    </div>
                
                </div>
                <div className="three">
                    <div className="one" >S</div>   
                    <div className="two">
                        <div className="desc-head">
                            SPRITED
                        </div>
                        <p>Frosh creates an energetic and spirited environment for the freshers for them to comfortably express their talents.</p>
                    </div>
                
                </div>
                <div className="three">
                    <div className="one" >H</div>   
                    <div className="two"  >
                        <div className="desc-head">
                            HUMBLE
                        </div>
                        <p>Frosh lays out a humble atmosphere for the freshers to approach them without hesitation.</p>
                    </div>
                
                </div>
            </div>
            <div className="faculty-team">
                <div className="faculty bg-triangle">

                    <Link to="/faculty" ><h1 className="faculty ">FACULTY</h1></Link>
                </div>
                <div className="team bg-triangle">

                    <Link to="/team" ><h1 className="team ">TEAM</h1></Link>
                </div>


                
            </div>
        </div>
    )

}

export default OurTeam