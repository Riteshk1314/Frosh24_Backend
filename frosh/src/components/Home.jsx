import React, { useRef } from "react";
import {Canvas, useFrame} from "@react-three/fiber";
import { useGLTF } from "@react-three/drei";
import {OrbitControls} from "@react-three/drei";

function Model() {
  const { scene } = useGLTF('../../public/modeljust.gltf');
  const ref = useRef();
  useFrame(() => {
    ref.current.rotation.y += 0.01;
  })
  return (
    <mesh position={[0,0,0]}>
  <primitive object={scene} scale={0.005} ref={ref} />
    </mesh>
  )
}
const Home = () => {

    return(
        <div className="home" id="Home">
            <div className="frosh-main-img">

            </div>
            <span className="compass">
                <Canvas>
                        <ambientLight intensity={100} />
                        <Model />
                      
                </Canvas>

            </span>
            <div className="frosh-tag">
                <h1>Navigating Through Timeless Trails</h1>
            </div>
        </div>
    )
}

export default Home