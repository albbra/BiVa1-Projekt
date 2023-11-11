cmake_minimum_required (VERSION 3.8)

# Enable Hot Reload for MSVC Compiler if supported.
if (POLICY CMP0141)
  cmake_policy(SET CMP0141 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

project ("Project1")

# Path to OpenCV 
set(OpenCV_DIR "D:/OpenCV/opencv/build/x64/vc16/lib")

# Find OpenCV package
find_package(OpenCV REQUIRED)

find_package(OpenCV REQUIRED COMPONENTS core highgui imgproc)

# Include directories for OpenCV headers
include_directories(${OpenCV_INCLUDE_DIRS})

# Link directories for OpenCV libraries
link_directories(${OpenCV_LIBRARY_DIRS})

# Add source files to the executable
add_executable (Project1 
    "Project1.cpp" 
    "Project1.h" 
    "Test.cpp" 
    "Test.h"
)

# Link the OpenCV library to your executable
target_link_libraries(Project1 PRIVATE ${OpenCV_LIBS})

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET Project1 PROPERTY CXX_STANDARD 20)
endif()