from vpython import *

# Set the scene
scene.width=800
scene.height=600
scene.forward=vector(6,-1,1)
scene.background=color.white


# Create the BNO055 board
bnoO55=box(length=0.5,width=0.38,height=0.04,opacity=.75,pos=vec(0,-0.065,0), color=vec(0.2,0.2,0.2))
bnoO55PCB=box(length=2,width=2.7,height=.13,opacity=.75,pos=vec(0,-0.13,0), color=vec(0,0.54,0.69))
bnoO55con1=box(length=0.25,width=1.2,height=1.03,opacity=.75,pos=vec(-0.85,-0.7025,0), color=vec(0.2,0.2,0.2))
bnoO55con2=box(length=0.25,width=1.6,height=1.03,opacity=.75,pos=vec(0.85,-0.7025,0), color=vec(0.2,0.2,0.2))

# Combine the BNO055 components into one object
bnoO55board=compound([bnoO55PCB,
                      bnoO55,
                      bnoO55con1,
                      bnoO55con2
                      ],
                     pos=vec(0,0,0), origin=vec(0,0,0))

# Create the Nordic board
nordicdkpcb=box(length=6.4,width=13.6,height=.13,opacity=.75,pos=vec(3.2,0,6.8), color=vec(0,0.8,0.5))
nrf52840=box(length=0.7,width=0.7,height=0.04,opacity=.75,pos=vec(1.9,0.085,2), color=vec(0.2,0.2,0.2))

# Create the connectors for the Nordic board
nordicdkcon1=box(length=.25,width=2.1,height=.7,opacity=.75,pos=vec(0.65,0.35,7.85), color=vec(.2,.2,.2))
nordicdkcon2=box(length=.25,width=2.1,height=.7,opacity=.75,pos=vec(0.65,0.35,5.5), color=vec(.2,.2,.2))
nordicdkcon3=box(length=.25,width=1.5,height=.7,opacity=.75,pos=vec(5.54,0.35,7.9), color=vec(.2,.2,.2))
nordicdkcon4=box(length=2.3,width=0.5,height=.7,opacity=.75,pos=vec(1.9,0.35,4), color=vec(.2,.2,.2))

# Combine the Nordic components into one object
nordicboard=compound([nordicdkpcb,
                      nrf52840,
                      nordicdkcon1,
                      nordicdkcon2,
                      nordicdkcon3,
                      nordicdkcon4
                      ],
                     pos=vec(-3.2,-2.55,-10), origin=vec(0,0,0))

# Create the bridge board
bridgepcb1=box(length=5.3,width=1.8,height=.13,opacity=.75,pos=vec(2.65,0,0.9), color=vec(1,0,0))
bridgepcb2=box(length=1.5,width=0.9,height=.13,opacity=.75,pos=vec(0.75,0,2.25), color=vec(1,0,0))
bridgepcb3=box(length=0.9,width=0.3,height=.13,opacity=.75,pos=vec(4.85,0,-0.15), color=vec(1,0,0))
bridgei2ccon=box(length=.25,width=2.6,height=1.2,opacity=.75,pos=vec(0.1,-0.685,1.3), color=vec(.2,.2,.2))
bridgepwcon=box(length=.25,width=2.1,height=1.2,opacity=.75,pos=vec(5,-0.685,0.78), color=vec(.2,.2,.2))

# Combine the bridge components into one object
bridge=compound([bridgepcb1,
                      bridgepcb2,
                      bridgepcb3,
                      bridgei2ccon,
                      bridgepwcon
                      ],
                     pos=vec(-2.65,-1.275,-0.9), origin=vec(0,0,0))


# Combine all the objects into one
fhObj=compound([bnoO55board,
                      nordicboard,
                      bridge
                      ],
                     pos=vec(0,0,0), origin=vec(0,0,0))

