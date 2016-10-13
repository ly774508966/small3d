find_path(SMALL3D_INCLUDE_DIR NAMES small3d PATHS include)
find_library(SMALL3D_LIBRARY NAMES small3d libsmall3d PATHS lib)

MESSAGE("** SMALL3D FOUND BY CONAN")
SET(SMALL3D_FOUND TRUE)
MESSAGE("** FOUND SMALL3D:  ${SMALL3D_LIBRARY}")
MESSAGE("** FOUND SMALL3D INCLUDE:  ${SMALL3D_INCLUDE_DIR}")

set(SMALL3D_INCLUDE_DIRS ${SMALL3D_INCLUDE_DIR})
set(SMALL3D_LIBRARIES ${SMALL3D_LIBRARY})

mark_as_advanced(SMALL3D_LIBRARY SMALL3D_INCLUDE_DIR)

set(SMALL3D_MAJOR_VERSION "1")
set(SMALL3D_MINOR_VERSION "0")
set(SMALL3D_PATCH_VERSION "8")
