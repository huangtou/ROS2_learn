// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from student_interfaces:action/Progress.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "student_interfaces/action/progress.h"


#ifndef STUDENT_INTERFACES__ACTION__DETAIL__PROGRESS__STRUCT_H_
#define STUDENT_INTERFACES__ACTION__DETAIL__PROGRESS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/Progress in the package student_interfaces.
typedef struct student_interfaces__action__Progress_Goal
{
  int32_t num;
} student_interfaces__action__Progress_Goal;

// Struct for a sequence of student_interfaces__action__Progress_Goal.
typedef struct student_interfaces__action__Progress_Goal__Sequence
{
  student_interfaces__action__Progress_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__action__Progress_Goal__Sequence;

// Constants defined in the message

/// Struct defined in action/Progress in the package student_interfaces.
typedef struct student_interfaces__action__Progress_Result
{
  int32_t sum;
} student_interfaces__action__Progress_Result;

// Struct for a sequence of student_interfaces__action__Progress_Result.
typedef struct student_interfaces__action__Progress_Result__Sequence
{
  student_interfaces__action__Progress_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__action__Progress_Result__Sequence;

// Constants defined in the message

/// Struct defined in action/Progress in the package student_interfaces.
typedef struct student_interfaces__action__Progress_Feedback
{
  double progress;
} student_interfaces__action__Progress_Feedback;

// Struct for a sequence of student_interfaces__action__Progress_Feedback.
typedef struct student_interfaces__action__Progress_Feedback__Sequence
{
  student_interfaces__action__Progress_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__action__Progress_Feedback__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "student_interfaces/action/detail/progress__struct.h"

/// Struct defined in action/Progress in the package student_interfaces.
typedef struct student_interfaces__action__Progress_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  student_interfaces__action__Progress_Goal goal;
} student_interfaces__action__Progress_SendGoal_Request;

// Struct for a sequence of student_interfaces__action__Progress_SendGoal_Request.
typedef struct student_interfaces__action__Progress_SendGoal_Request__Sequence
{
  student_interfaces__action__Progress_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__action__Progress_SendGoal_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/Progress in the package student_interfaces.
typedef struct student_interfaces__action__Progress_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} student_interfaces__action__Progress_SendGoal_Response;

// Struct for a sequence of student_interfaces__action__Progress_SendGoal_Response.
typedef struct student_interfaces__action__Progress_SendGoal_Response__Sequence
{
  student_interfaces__action__Progress_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__action__Progress_SendGoal_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  student_interfaces__action__Progress_SendGoal_Event__request__MAX_SIZE = 1
};
// response
enum
{
  student_interfaces__action__Progress_SendGoal_Event__response__MAX_SIZE = 1
};

/// Struct defined in action/Progress in the package student_interfaces.
typedef struct student_interfaces__action__Progress_SendGoal_Event
{
  service_msgs__msg__ServiceEventInfo info;
  student_interfaces__action__Progress_SendGoal_Request__Sequence request;
  student_interfaces__action__Progress_SendGoal_Response__Sequence response;
} student_interfaces__action__Progress_SendGoal_Event;

// Struct for a sequence of student_interfaces__action__Progress_SendGoal_Event.
typedef struct student_interfaces__action__Progress_SendGoal_Event__Sequence
{
  student_interfaces__action__Progress_SendGoal_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__action__Progress_SendGoal_Event__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/Progress in the package student_interfaces.
typedef struct student_interfaces__action__Progress_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} student_interfaces__action__Progress_GetResult_Request;

// Struct for a sequence of student_interfaces__action__Progress_GetResult_Request.
typedef struct student_interfaces__action__Progress_GetResult_Request__Sequence
{
  student_interfaces__action__Progress_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__action__Progress_GetResult_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "student_interfaces/action/detail/progress__struct.h"

/// Struct defined in action/Progress in the package student_interfaces.
typedef struct student_interfaces__action__Progress_GetResult_Response
{
  int8_t status;
  student_interfaces__action__Progress_Result result;
} student_interfaces__action__Progress_GetResult_Response;

// Struct for a sequence of student_interfaces__action__Progress_GetResult_Response.
typedef struct student_interfaces__action__Progress_GetResult_Response__Sequence
{
  student_interfaces__action__Progress_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__action__Progress_GetResult_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
// already included above
// #include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  student_interfaces__action__Progress_GetResult_Event__request__MAX_SIZE = 1
};
// response
enum
{
  student_interfaces__action__Progress_GetResult_Event__response__MAX_SIZE = 1
};

/// Struct defined in action/Progress in the package student_interfaces.
typedef struct student_interfaces__action__Progress_GetResult_Event
{
  service_msgs__msg__ServiceEventInfo info;
  student_interfaces__action__Progress_GetResult_Request__Sequence request;
  student_interfaces__action__Progress_GetResult_Response__Sequence response;
} student_interfaces__action__Progress_GetResult_Event;

// Struct for a sequence of student_interfaces__action__Progress_GetResult_Event.
typedef struct student_interfaces__action__Progress_GetResult_Event__Sequence
{
  student_interfaces__action__Progress_GetResult_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__action__Progress_GetResult_Event__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "student_interfaces/action/detail/progress__struct.h"

/// Struct defined in action/Progress in the package student_interfaces.
typedef struct student_interfaces__action__Progress_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  student_interfaces__action__Progress_Feedback feedback;
} student_interfaces__action__Progress_FeedbackMessage;

// Struct for a sequence of student_interfaces__action__Progress_FeedbackMessage.
typedef struct student_interfaces__action__Progress_FeedbackMessage__Sequence
{
  student_interfaces__action__Progress_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} student_interfaces__action__Progress_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // STUDENT_INTERFACES__ACTION__DETAIL__PROGRESS__STRUCT_H_
