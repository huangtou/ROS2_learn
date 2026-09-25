# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target student_interfaces::student_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${student_interfaces_TARGETS}.
if(student_interfaces_TARGETS AND NOT TARGET student_interfaces::student_interfaces)
  add_library(student_interfaces::student_interfaces INTERFACE IMPORTED)
  set_target_properties(student_interfaces::student_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${student_interfaces_TARGETS}")
endif()
