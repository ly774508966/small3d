# Only building shared library, since the static library would not work
from conans import ConanFile, CMake, os
import os

class Small3dConan(ConanFile):
    name = "small3d"
    version = "1.0.3"
    generators = "cmake"
    settings = "os", "arch", "build_type", "compiler"
    url="http://github.com/coding3d/small3d"
    requires = "SDL2/2.0.4@lasote/stable","SDL2_ttf/2.0.14@lasote/stable","glew/1.13.0@coding3d/ci","libpng/1.6.23@lasote/stable","zlib/1.2.8@lasote/stable","gtest/1.7.0@lasote/stable"
    license="https://github.com/coding3d/small3d/blob/master/LICENSE"
    exports = "*"

    def config(self):
        try: # Try catch can be removed when conan 0.8 is released
            del self.settings.compiler.libcxx
        except:
            pass

    def build(self):
        cmake = CMake(self.settings)

        try:
            if self.settings.os == "Windows":
                self.run("cd .. && rd /s /q _build")
            else:
                self.run("cd .. && rm -rf _build")
        except:
            pass

        self.run("cd .. && mkdir _build")
        cd_build = "cd ../_build"
        self.run("%s && cmake .. %s" % (cd_build, cmake.command_line))
        self.run("%s && cmake --build . %s" % (cd_build, cmake.build_config))

    def package(self):
        # Copying headers
        self.copy("../*.hpp", "./include", "..", keep_path=True)

        if self.settings.os == "Windows":
            self.copy(pattern="*.dll", dst="bin", src=self.ZIP_FOLDER_NAME, keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src=self.ZIP_FOLDER_NAME, keep_path=False)
        else:
            if self.settings.os == "Macos":
                self.copy(pattern="*.dylib", dst="lib", keep_path=False)
            else:
                self.copy(pattern="*.so*", dst="lib", src="..", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['smal3d']