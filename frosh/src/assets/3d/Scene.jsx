

import React from 'react'
import { useGLTF } from '@react-three/drei'

export default function Model(props) {
  const { nodes, materials } = useGLTF('./scene.gltf')
  return (
    <group {...props} dispose={null}>
      <group rotation={[-Math.PI / 2, 0, 0]}>
        <group rotation={[-Math.PI, 0, 0]} scale={0.01}>
          <group rotation={[Math.PI / 2, 0, 0]} scale={[191.768, 191.768, 68.271]}>
            <mesh geometry={nodes.Tire_Tire_0.geometry} material={materials.Tire} />
            <mesh geometry={nodes.Tire_Tire_0_1.geometry} material={materials.Tire} />
            <mesh geometry={nodes.Tire_Tire_0_2.geometry} material={materials.Tire} />
          </group>
          <group position={[0, -59.055, 0]} rotation={[Math.PI / 2, 0, 0]} scale={100}>
            <mesh geometry={nodes.wheel_Wheel_0.geometry} material={materials.Wheel} />
            <mesh geometry={nodes.wheel_Wheel_0_1.geometry} material={materials.Wheel} />
            <mesh geometry={nodes.wheel_Bolts_0.geometry} material={materials.Bolts} />
          </group>
        </group>
      </group>
    </group>
  )
}

useGLTF.preload('/scene.gltf')
