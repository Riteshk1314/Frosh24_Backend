import React, {useState} from "react";
import logo from "../assets/frosh-white.png"
import { Link} from 'react-router-dom'
import { HashLink } from 'react-router-hash-link'

const Nav=()=>{
    const [navMobile ,setNavMobile] = useState(false)
    const[width , setWidth] = useState(window.innerWidth)

    const toggleNavOpen = ()=>{
        if(navMobile){
            setNavMobile(false)
        }
        else{
            setNavMobile(true)
        }
    }
    return(
        <nav className={`navbar background ${navMobile ? "" : "h-nav-resp"} `}>

            <div className="logo"><Link to="/"><img src={logo} alt="logo" /></Link></div>
            <ul className={`nav-list another ${navMobile? "" : "v-class-resp"}`}>
                <li><Link to="/">HOME</Link></li>
                <li><HashLink to="#event" smooth >EVENT</HashLink></li>
                <li><HashLink to="#map" smooth>MAP</HashLink></li>
                <li><HashLink to="#about" smooth>ABOUT</HashLink></li>
                <li><HashLink to="#sponsors" smooth >SPONSORS</HashLink></li>
            </ul>
            <div className={`rightNav ${navMobile? "" : "v-class-resp"} `}>
                <Link to="/login">GET TICKETS</Link>
            </div>

            <div className={`burger ${navMobile? "burger-top":""}`} onClick={toggleNavOpen}>
            <div className="line"></div>
            <div className="line"></div>
            <div className="line"></div>
            </div>
    </nav>
    )
}

export default Nav
