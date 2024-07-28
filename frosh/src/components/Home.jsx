import React, { useRef } from "react";
import {Canvas, useFrame} from "@react-three/fiber";
import { Environment, useGLTF } from "@react-three/drei";
import {OrbitControls} from "@react-three/drei";
import { AmbientLight, MeshBasicMaterial } from "three";

function Model() {
  const { scene } = useGLTF('../../public/compass web.gltf');
  const ref = useRef();
  useFrame(() => {
      ref.current.position.y=0.52;
      const y = window.scrollY;
      console.log(y);
    if (y>=0 && y<=1){
      ref.current.rotation.y+=0.01;
    }
    else if(y>=2009 && y<=2010){
      ref.current.rotation.y-=0.01;
    }
    else{
      ref.current.rotation.y = -y * 0.0062;
      ref.current.position.x = Math.sin(y*0.003112) * 1.2 ;
      
    }

    

  })
  return (
    <mesh position={[0,0,0]}>
  <primitive object={scene} scale={0.3} ref={ref} />
    </mesh>
  )
}
const Home = () => {

    return(
        <div className="home" id="Home">
            <div className="main_landing">

            </div>
            <span className="compass">
                <Canvas>
                 <Environment preset="studio" environmentIntensity={0.5} />
                        <Model />
                        <OrbitControls enablePan={false} enableZoom={false} enableDamping={true} /> 
                      
                </Canvas>

            </span>

         
            <div className="frosh-tag">
                <h1>Navigating Through Timeless Trails</h1>
            </div>
        </div>
    )
}

export default Home