import React, {useState} from "react";
import logo from "../assets/frosh-white.png"
import { Link} from 'react-router-dom'
import { HashLink } from 'react-router-hash-link'
// import { NavLink } from "react-router-dom";

const Nav=(props)=>{
    const [navMobile ,setNavMobile] = useState(false)
    const[width , setWidth] = useState(window.innerWidth)
    const [navBlur, setNavBlur] = useState(false)

    const toggleBlur = ()=>{
        if(window.scrollY>90){
            setNavBlur(true)
        }
        else{
            setNavBlur(false)
        }
        
    }
    
    window.addEventListener('scroll',toggleBlur)

    const toggleNavOpen = ()=>{
        if(navMobile){
            setNavMobile(false)
        }
        else{
            setNavMobile(true)
        }
    }
    return(
        <nav className={`navbar background ${navMobile ? "" : "h-nav-resp"} ${navBlur? "bg-blur" : ""} `}>

            <div className="logo"><HashLink to="/#Home" smooth ><img src={logo} alt="logo"  /></HashLink></div>
            <ul className={`nav-list another ${navMobile? "" : "v-class-resp"}`}>
                <li><Link to="/">HOME</Link></li>
                <li><HashLink activeStyle={{ color:'#5754a8' }} to="#login" smooth >EVENT</HashLink></li>
                <li><HashLink  activeStyle={{ color:'#5754a8' }} to="#map" smooth>MAP</HashLink></li>
                <li><HashLink activeStyle={{ color:'#5754a8' }} to="#about" smooth>ABOUT</HashLink></li>
                <li><HashLink activeStyle={{ color:'#5754a8' }} to="#sponsors" smooth >SPONSORS</HashLink></li>
            </ul>
            <div className={`rightNav ${navMobile? "" : "v-class-resp"} `}>
                {(!props.isLoggedIn)? (<Link to="/login">GET TICKETS</Link>) : (<Link to="/dashboard"><a href="/dashboard">DASHBOARD</a></Link>)}
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
