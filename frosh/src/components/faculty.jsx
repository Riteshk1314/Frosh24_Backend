import React from 'react'
import Nav from './nav'

const faculty = () => {
    return (
        <>
            <Nav />
            <div className='bg-faculty font-faculty'>

                    <div className="container">
                        <div className="section-faculty ">
                            <h1>Faculty</h1>
                            <div className="faculty-members">
                                <div className="member faculty1">
                                    <div className="name">DR. MD SINGH,<br />
                                        President Frosh. EIED</div>
                                </div>
                                <div className="member faculty2">
                                    <div className="name">DR. AVINASH CHANDRA<br />
                                        Vice President Frosh. CHED
                                        </div>
                                </div>
                                <div className="member faculty3">
                                    <div className="name">DR. DEVENDER KUMAR,<br />
                                    Vice President Frosh. MEE
                                        </div>
                                </div>
                            </div>
                            <div className="faculty-members">
                                <div className="member faculty4">
                                    <div className="name">DR. HEMDUTT JOSHI,<br />
                                    Vice President Frosh. ECED</div>
                                </div>
                                <div class="member faculty5">
                                    <div class="name">DR. TARUNPREET BHATIA,<br />
                                    Vice President Frosh. CSED</div>
                                </div>
                                <div class="member faculty6">
                                    <div class="name">DR. VISHAL GUPTA,<br />
                                    Vice President Frosh. MEE
                                    </div>
                                
                                </div>
                            </div>
                        </div>
                    </div>
            </div>
        
        </>
    )

}

export default faculty
