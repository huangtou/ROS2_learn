// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from student_interfaces:msg/Student.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "student_interfaces/msg/student.hpp"


#ifndef STUDENT_INTERFACES__MSG__DETAIL__STUDENT__TRAITS_HPP_
#define STUDENT_INTERFACES__MSG__DETAIL__STUDENT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "student_interfaces/msg/detail/student__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace student_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Student & msg,
  std::ostream & out)
{
  out << "{";
  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << ", ";
  }

  // member: age
  {
    out << "age: ";
    rosidl_generator_traits::value_to_yaml(msg.age, out);
    out << ", ";
  }

  // member: height
  {
    out << "height: ";
    rosidl_generator_traits::value_to_yaml(msg.height, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Student & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }

  // member: age
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "age: ";
    rosidl_generator_traits::value_to_yaml(msg.age, out);
    out << "\n";
  }

  // member: height
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "height: ";
    rosidl_generator_traits::value_to_yaml(msg.height, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Student & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace student_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use student_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const student_interfaces::msg::Student & msg,
  std::ostream & out, size_t indentation = 0)
{
  student_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use student_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const student_interfaces::msg::Student & msg)
{
  return student_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<student_interfaces::msg::Student>()
{
  return "student_interfaces::msg::Student";
}

template<>
inline const char * name<student_interfaces::msg::Student>()
{
  return "student_interfaces/msg/Student";
}

template<>
struct has_fixed_size<student_interfaces::msg::Student>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<student_interfaces::msg::Student>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<student_interfaces::msg::Student>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // STUDENT_INTERFACES__MSG__DETAIL__STUDENT__TRAITS_HPP_
