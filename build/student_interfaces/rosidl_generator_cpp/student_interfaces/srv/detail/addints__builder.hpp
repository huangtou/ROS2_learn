// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from student_interfaces:srv/Addints.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "student_interfaces/srv/addints.hpp"


#ifndef STUDENT_INTERFACES__SRV__DETAIL__ADDINTS__BUILDER_HPP_
#define STUDENT_INTERFACES__SRV__DETAIL__ADDINTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "student_interfaces/srv/detail/addints__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace student_interfaces
{

namespace srv
{

namespace builder
{

class Init_Addints_Request_num2
{
public:
  explicit Init_Addints_Request_num2(::student_interfaces::srv::Addints_Request & msg)
  : msg_(msg)
  {}
  ::student_interfaces::srv::Addints_Request num2(::student_interfaces::srv::Addints_Request::_num2_type arg)
  {
    msg_.num2 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::student_interfaces::srv::Addints_Request msg_;
};

class Init_Addints_Request_num1
{
public:
  Init_Addints_Request_num1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Addints_Request_num2 num1(::student_interfaces::srv::Addints_Request::_num1_type arg)
  {
    msg_.num1 = std::move(arg);
    return Init_Addints_Request_num2(msg_);
  }

private:
  ::student_interfaces::srv::Addints_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::student_interfaces::srv::Addints_Request>()
{
  return student_interfaces::srv::builder::Init_Addints_Request_num1();
}

}  // namespace student_interfaces


namespace student_interfaces
{

namespace srv
{

namespace builder
{

class Init_Addints_Response_sum
{
public:
  Init_Addints_Response_sum()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::student_interfaces::srv::Addints_Response sum(::student_interfaces::srv::Addints_Response::_sum_type arg)
  {
    msg_.sum = std::move(arg);
    return std::move(msg_);
  }

private:
  ::student_interfaces::srv::Addints_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::student_interfaces::srv::Addints_Response>()
{
  return student_interfaces::srv::builder::Init_Addints_Response_sum();
}

}  // namespace student_interfaces


namespace student_interfaces
{

namespace srv
{

namespace builder
{

class Init_Addints_Event_response
{
public:
  explicit Init_Addints_Event_response(::student_interfaces::srv::Addints_Event & msg)
  : msg_(msg)
  {}
  ::student_interfaces::srv::Addints_Event response(::student_interfaces::srv::Addints_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::student_interfaces::srv::Addints_Event msg_;
};

class Init_Addints_Event_request
{
public:
  explicit Init_Addints_Event_request(::student_interfaces::srv::Addints_Event & msg)
  : msg_(msg)
  {}
  Init_Addints_Event_response request(::student_interfaces::srv::Addints_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_Addints_Event_response(msg_);
  }

private:
  ::student_interfaces::srv::Addints_Event msg_;
};

class Init_Addints_Event_info
{
public:
  Init_Addints_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Addints_Event_request info(::student_interfaces::srv::Addints_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_Addints_Event_request(msg_);
  }

private:
  ::student_interfaces::srv::Addints_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::student_interfaces::srv::Addints_Event>()
{
  return student_interfaces::srv::builder::Init_Addints_Event_info();
}

}  // namespace student_interfaces

#endif  // STUDENT_INTERFACES__SRV__DETAIL__ADDINTS__BUILDER_HPP_
