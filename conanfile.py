from conans import ConanFile, CMake, tools
import os

class ConanLibtorchConan(ConanFile):
    name = "conan_libtorch"
    version = "1.8.0"
    settings = "os", "compiler", "build_type", "arch"

    def build(self):
        tools.get("https://download.pytorch.org/libtorch/cpu/libtorch-cxx11-abi-shared-with-deps-1.8.0%2Bcpu.zip")

    def package(self):
        self.copy("*", src="libtorch/")

    def package_info(self):
        libs_list = self.collect_libs()
        undesired_libs = ['gtest_main', "gtest", 'gmock', 'gmock_main']
        libs_list = [x for x in libs_list if x not in undesired_libs]
        print(libs_list)
        self.cpp_info.libs = libs_list
        self.cpp_info.includedirs = ['include', 'include/torch/csrc/api/include']
        self.cpp_info.bindirs = ['bin']
        self.cpp_info.libdirs = ['lib']

