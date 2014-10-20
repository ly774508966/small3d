small3d 
=======
*A small, no fuss, 3D game engine*

![Screen capture from the first game that runs on small3d](https://cloud.githubusercontent.com/assets/875167/4695565/ca5fafb2-5808-11e4-8a81-d186db8b335c.png)

This is a free, open-source, minimalistic 3D game engine, developed in C++ and based on modern OpenGL. It is meant for those who are in a hurry to produce something playable, but prefer to understand what is happening under the hood rather than use a technology that abstracts the low-level details away.

It has been derived from a simple game which has been under development for more than a year, as a learning exercise (introduction: http://goo.gl/itn6x5, blog: http://goo.gl/7hCTPA). I have decided to separate the engine from the game already, rather than finishing the project first. I think that this will help the engine mature faster and will simplify the development of the game.

What actually made me take the plunge though, was that I discovered the great C++ dependency management tool and service that is biicode :) (http://www.biicode.com/) So I have configured the engine’s files to be served from there (many thanks to the other biicode members who have set up the libraries I am using). So now my project setup tasks involve something like this: http://goo.gl/CJPnkK, which is much faster and simpler than what I had to do before, which was this: http://goo.gl/fUZbBa

Over time, more information will be provided about this project and how it can be used, but here are some items to begin with:

API documentation: http://small3d.org/namespacesmall3d.html

Block on biicode: http://www.biicode.com/dimitrikourk/dimitrikourk/small3d/master

GitHub source: https://github.com/dimitrikourk/small3d

Original branch of the game development project:
https://github.com/dimitrikourk/CrossPlatform3DLearning

biicode-adapted branch of the game development project, which now uses the engine:
"samplegame" folder within the block (used to be a separate block)

Note about MinGW
----------------
If you are compiling with MinGW, please note that it has a little bug and requires a small modification (at least my installation does, which was downloaded on the 20/10/2014 and runs gcc 4.8.1).

The engine uses certain features which obliged me to enable the C++11 switch in CMakeLists.txt. But then I could not compile. I managed to solve the problem by opening the io.h file, and going to line 300, more or less, where the following code is present:

mingw has a bug when using the c++11 switch:
http://sourceforge.net/p/mingw/bugs/2024/

_CRT_INLINE off64_t lseek64 (int, off64_t, int);
_CRT_INLINE off64_t lseek64 (int fd, off64_t offset, int whence) {
  return _lseeki64(fd, (__int64) offset, whence);

By changing all the occurrences of off64_t to _off64_t here, the issue was resolved.

Note about 3D models and textures
---------------------------------

For the time being, the engine can only read 3D
models from Wavefront .obj files. There are many
ways to create such a file, but I am exporting them
from Blender.

When exporting the models to Wavefront .obj files,
make sure you set the options "Include Normals",
"Triangulate Faces", and "Keep Vertex Order".
Only one object should be exported to each
Wavefront file, because the engine cannot read
more than one. The model has to have been set to
have smooth shading in Blender and double vertices
have to have been deleted before the export.
Otherwise, when rendering with shaders, lighting
will not work, since there will be multiple
normals for each vertex and, with indexed drawing,
the normals listed later in the exported file
for some vertices will overwrite the previous
ones.

If a texture has been created, the option "Include
UVs" must also be set. The texture should be saved
as a PNG file, since this is the format that can
be read by the program. The PNG file can have no
transparency information stored (in my case, in 
order to achieve this, I load it in Gimp, select 
Image > Flatten Image and then re-export it as a
PNG file from there).

The engine also supports manually created bounding
boxes for collision detection. In order to create
these in Blender for example, just place them in
the preferred position over the model and export
them to Wavefront separately from the model, only 
with the options "Apply Modifiers", "Include Edges",
"Objects as OBJ Objects" and "Keep Vertex Order".
On the contrary to what is the case when exporting
the model itself, more than one bounding box objects 
can be exported to the same Wavefront file.


