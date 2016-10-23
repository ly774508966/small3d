from conans import ConanFile, CMake, os
import os, subprocess

class Small3dConan(ConanFile):
    name = "small3d"
    version = "1.0.10"
    ZIP_FOLDER_NAME = "%s-%s" % (name, version)
    generators = "cmake"
    settings = "os", "arch", "build_type", "compiler"
    url="http://github.com/dimi309/small3d"
    requires = "SDL2/2.0.4@lasote/stable","SDL2_ttf/2.0.14@coding3d/ci","glew/2.0.0@coding3d/stable", \
        "libpng/1.6.23@lasote/stable","zlib/1.2.8@lasote/stable","glm/0.9.7.6@dlarudgus20/stable", \
        "vorbis/1.3.5@coding3d/stable", "portaudio/rc.v190600.20161001@jgsogo/stable"
    default_options = "glew:shared=False"
    license="https://github.com/dimi309/small3d/blob/master/LICENSE"
    exports = "CMakeLists.txt", "small3d/*", "FindSMALL3D.cmake", "cmake/*"

    def linux_package_installed(self, package):
        p = subprocess.Popen(['dpkg', '-s', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return 'install ok' in out

    def ensure_linux_dependency(self, package):
        if not self.linux_package_installed(package):
            self.output.warn(package + " is not installed in this machine! Conan will try to install it.")
            self.run("sudo apt-get update && sudo apt-get install -y " + package)
            if not self.linux_package_installed(package):
                self.output.error(package + " Installation doesn't work... install it manually and try again")
                exit(1)

    def system_requirements(self):
        if self.settings.os == "Linux":
            self.ensure_linux_dependency("libjack-dev")

    def build(self):
        cmake = CMake(self.settings)
        self.run("cmake %s -DBUILD_WITH_CONAN=TRUE %s" % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("FindSMALL3D.cmake", ".", ".")
        self.copy(pattern="*", dst="shaders", src="small3d/resources/shaders", keep_path=True)
        self.copy(pattern="*.hpp", dst="include", src="small3d/include", keep_path=True)

        if self.settings.os == "Windows":
            self.copy(pattern="*.dll", dst="bin", keep_path=False)
            self.copy(pattern="*.lib", dst="lib", keep_path=False)
        else:
            if self.settings.os == "Macos":
                self.copy(pattern="*.a", dst="lib", keep_path=False)
            else:
                self.copy(pattern="*.so*", dst="lib", keep_path=False)
                self.copy(pattern="*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['small3d']
        if self.settings.os == "Windows":
            self.cpp_info.exelinkflags.append('/NODEFAULTLIB:LIBCMTD')
            self.cpp_info.exelinkflags.append('/NODEFAULTLIB:LIBCMT')
        elif self.settings.os == "Macos":
            self.cpp_info.cppflags.append("-std=c++11")
            self.cpp_info.cppflags.append("-stdlib=libc++")
        else:
            self.cpp_info.cppflags.append("-std=c++11")
            self.cpp_info.cppflags.append("-Wl,--no-as-needed")
            self.cpp_info.exelinkflags.append("-ljack -lasound")
