clone this repo into the home folder of the virtual machine.

It does not need to be in a workspace at the moment - you will just load the world file into ignition using a command.

Once it is cloned you can load it into the simulator with the command (assuming the terminal is in the home folder - adjusted the relative path to the file if neccessary)

ign gazebo assess_world/assess2022.sdf -v 4

I mentioned an issue with lidar simulators in class. This appears to be an issue with the graphics acceleraration on Mac computers only, so if your computer is windows it should all work fine already.

If you are running the virtual machine on Mac, then you need to enable 3d acceleration in the graphics setting for the virtual machine. Your virtual machine will need to be shut down to be able to do this. Once that is enabled you will need to add the text below to the end of the .bashrc file in the ubuntu virtual machine

\# set_mesa_env

\# Configure the Mesa Environment
\# https://docs.mesa3d.org/envvars.html

\# Core Mesa environment variables
export MESA_DEBUG=1
export MESA_GL_VERSION_OVERRIDE=4.1
export MESA_GLSL_VERSION_OVERRIDE=410
export MESA_EXTENSION_OVERRIDE="\
  -GL_ARB_buffer_storage \
  -GL_ARB_multi_draw_indirect \
  -GL_ARB_texture_buffer_range \
  -GL_ARB_compute_shader \
  -GL_ARB_ES3_compatibility \
  "

I have not been able to check in an M1 Mac yet, but would expect the same is necessary for that. Should get access to one at the end of this week to do some tests.





