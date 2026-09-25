// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from student_interfaces:srv/Addints.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "student_interfaces/srv/addints.h"


#ifndef STUDENT_INTERFACES__SRV__DETAIL__ADDINTS__STRUCT_H_
#define STUDENT_INTERFACES__SRV__DETAIL__ADDINTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Addints in the package student_interfaces.
typedef struct student_interfaces__srv__Addints_Request
{
  int32_t num1;
  int32_t num2;
} student_interfaces__srv__Addints_Request;

// Struct for a sequence of student_interfaces__srv__Addints_Request.
typedef struct student_interfaces__srv__Addints_Request__Sequence
{
  student_interfaces__srv__Addints_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__srv__Addints_Request__Sequence;

// Constants defined in the message

/// Struct defined in srv/Addints in the package student_interfaces.
typedef struct student_interfaces__srv__Addints_Response
{
  int32_t sum;
} student_interfaces__srv__Addints_Response;

// Struct for a sequence of student_interfaces__srv__Addints_Response.
typedef struct student_interfaces__srv__Addints_Response__Sequence
{
  student_interfaces__srv__Addints_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__srv__Addints_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  student_interfaces__srv__Addints_Event__request__MAX_SIZE = 1
};
// response
enum
{
  student_interfaces__srv__Addints_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/Addints in the package student_interfaces.
typedef struct student_interfaces__srv__Addints_Event
{
  service_msgs__msg__ServiceEventInfo info;
  student_interfaces__srv__Addints_Request__Sequence request;
  student_interfaces__srv__Addints_Response__Sequence response;
} student_interfaces__srv__Addints_Event;

// Struct for a sequence of student_interfaces__srv__Addints_Event.
typedef struct student_interfaces__srv__Addints_Event__Sequence
{
  student_interfaces__srv__Addints_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__srv__Addints_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // STUDENT_INTERFACES__SRV__DETAIL__ADDINTS__STRUCT_H_
