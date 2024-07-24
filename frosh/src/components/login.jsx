import React from "react";

const Login = (props) => {
    return(
        <div className="login">
          <div className="login-main">
            <div className="overlay">
              <div className="box">
                <form onSubmit={props.handleSubmit}>
                  <div className="login-input">

                    <h4>USERNAME</h4>
                    <input
                      type="text"
                      value={props.username}
                      onChange={props.handleUsernameChange}
                      placeholder="Username"
                    />
                  </div>
                  <div className="login-input">
                    <h4>PASSWORD</h4>
                    <input
                      type="password"
                      value={props.password}
                      onChange={props.handlePasswordChange}
                      placeholder="Password"
                    />

                  </div>
                  <div className="forgot">
                    <a href="#" className="forgot">Forgot Password?</a>
                  </div>
                    <button type="submit" className="log">Login</button>
                </form>
              </div>
            </div>
          </div>
        </div>
    )
}

export default Login