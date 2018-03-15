cmake_minimum_required(VERSION 3.3 FATAL_ERROR)  # 3.3: EP_add(DEPENDS interfacelib

project({{ cookiecutter.project_slug }})
set({{ cookiecutter.project_slug }}_AUTHORS      "{{ cookiecutter.full_name }}")
set({{ cookiecutter.project_slug }}_DESCRIPTION  "{{ cookiecutter.project_short_description }}")
set({{ cookiecutter.project_slug }}_URL          "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}")
set({{ cookiecutter.project_slug }}_LICENSE      "{{ cookiecutter.open_source_license }}")

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

############################  Options: Build How?  #############################
include(psi4OptionsTools)
option_with_default(CMAKE_BUILD_TYPE "Build type (Release or Debug)" Release)
option_with_default(CMAKE_INSTALL_LIBDIR "Directory to which libraries installed" lib)
option_with_default(PYMOD_INSTALL_LIBDIR "Location within CMAKE_INSTALL_LIBDIR to which python modules are installed" /)
option_with_default(CMAKE_INSTALL_MESSAGE "Specify verbosity of installation messages" LAZY)

########################  Process & Validate Options  ##########################
include(autocmake_safeguards)
include(custom_color_messages)

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
    set(CMAKE_INSTALL_PREFIX "/usr/local/{{ cookiecutter.project_slug }}" CACHE PATH "Install path" FORCE)
endif()
message(STATUS "{{ cookiecutter.project_slug }} install: ${CMAKE_INSTALL_PREFIX}")

set(Python_ADDITIONAL_VERSIONS 3.7 3.6 3.5)  # adjust with CMake minimum FindPythonInterp
find_package(PythonLibsNew 2.7 REQUIRED)
message(STATUS "${Cyan}Found Python ${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}${ColourReset}: ${PYTHON_EXECUTABLE} (found version ${PYTHON_VERSION_STRING})")

################################  Main Project  ################################
include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

#add_subdirectory(doc)

# <<<  Version  >>>
add_custom_target(update_version ALL
                  COMMAND ${PYTHON_EXECUTABLE} {{ cookiecutter.project_slug }}/versioner.py 
                                               --metaout ${CMAKE_CURRENT_BINARY_DIR}/metadata.py
                                               --cmakeout ${CMAKE_CURRENT_BINARY_DIR}/metadata.cmake
                  COMMAND cmake -DWTO="${CMAKE_CURRENT_BINARY_DIR}/${CMAKECONFIG_INSTALL_DIR}"
                                -DPN="{{ cookiecutter.project_slug }}"
                                -P ${CMAKE_CURRENT_BINARY_DIR}/metadata.cmake
                  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                  COMMENT "Generating version info")
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/metadata.py
        DESTINATION ${CMAKE_INSTALL_LIBDIR}${PYMOD_INSTALL_LIBDIR}/{{ cookiecutter.project_slug }})

# <<<  Install  >>>

set(PN ${PROJECT_NAME})

install(DIRECTORY {{ cookiecutter.project_slug }} 
        DESTINATION ${CMAKE_INSTALL_LIBDIR}${PYMOD_INSTALL_LIBDIR}
        USE_SOURCE_PERMISSIONS
        FILES_MATCHING PATTERN "*.py")

install(DIRECTORY tests
        DESTINATION ${CMAKE_INSTALL_LIBDIR}${PYMOD_INSTALL_LIBDIR}/{{ cookiecutter.project_slug }}
        USE_SOURCE_PERMISSIONS
        FILES_MATCHING PATTERN "*.py")

configure_file({{ cookiecutter.project_slug }}/__init__.py {{ cookiecutter.project_slug }}/__init__.py @ONLY)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/{{ cookiecutter.project_slug }}/__init__.py
        DESTINATION ${CMAKE_INSTALL_LIBDIR}${PYMOD_INSTALL_LIBDIR}/{{ cookiecutter.project_slug }})

# <<<  Export Config  >>>

# GNUInstallDirs "DATADIR" wrong here; CMake search path wants "share".
set(CMAKECONFIG_INSTALL_DIR "share/cmake/${PN}")
configure_package_config_file(cmake/${PN}Config.cmake.in
                              "${CMAKE_CURRENT_BINARY_DIR}/${PN}Config.cmake"
                              INSTALL_DESTINATION ${CMAKECONFIG_INSTALL_DIR})

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${PN}Config.cmake
              ${CMAKE_CURRENT_BINARY_DIR}/${PN}ConfigVersion.cmake
        DESTINATION ${CMAKECONFIG_INSTALL_DIR})

