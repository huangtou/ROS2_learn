// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from student_interfaces:msg/Student.idl
// generated code does not contain a copyright notice
#include "student_interfaces/msg/detail/student__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"

bool
student_interfaces__msg__Student__init(student_interfaces__msg__Student * msg)
{
  if (!msg) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__init(&msg->name)) {
    student_interfaces__msg__Student__fini(msg);
    return false;
  }
  // age
  // height
  return true;
}

void
student_interfaces__msg__Student__fini(student_interfaces__msg__Student * msg)
{
  if (!msg) {
    return;
  }
  // name
  rosidl_runtime_c__String__fini(&msg->name);
  // age
  // height
}

bool
student_interfaces__msg__Student__are_equal(const student_interfaces__msg__Student * lhs, const student_interfaces__msg__Student * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  // age
  if (lhs->age != rhs->age) {
    return false;
  }
  // height
  if (lhs->height != rhs->height) {
    return false;
  }
  return true;
}

bool
student_interfaces__msg__Student__copy(
  const student_interfaces__msg__Student * input,
  student_interfaces__msg__Student * output)
{
  if (!input || !output) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  // age
  output->age = input->age;
  // height
  output->height = input->height;
  return true;
}

student_interfaces__msg__Student *
student_interfaces__msg__Student__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  student_interfaces__msg__Student * msg = (student_interfaces__msg__Student *)allocator.allocate(sizeof(student_interfaces__msg__Student), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(student_interfaces__msg__Student));
  bool success = student_interfaces__msg__Student__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
student_interfaces__msg__Student__destroy(student_interfaces__msg__Student * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    student_interfaces__msg__Student__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
student_interfaces__msg__Student__Sequence__init(student_interfaces__msg__Student__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  student_interfaces__msg__Student * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(student_interfaces__msg__Student)) {
      return false;
    }
    data = (student_interfaces__msg__Student *)allocator.zero_allocate(size, sizeof(student_interfaces__msg__Student), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = student_interfaces__msg__Student__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        student_interfaces__msg__Student__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
student_interfaces__msg__Student__Sequence__fini(student_interfaces__msg__Student__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      student_interfaces__msg__Student__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

student_interfaces__msg__Student__Sequence *
student_interfaces__msg__Student__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  student_interfaces__msg__Student__Sequence * array = (student_interfaces__msg__Student__Sequence *)allocator.allocate(sizeof(student_interfaces__msg__Student__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = student_interfaces__msg__Student__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
student_interfaces__msg__Student__Sequence__destroy(student_interfaces__msg__Student__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    student_interfaces__msg__Student__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
student_interfaces__msg__Student__Sequence__are_equal(const student_interfaces__msg__Student__Sequence * lhs, const student_interfaces__msg__Student__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!student_interfaces__msg__Student__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
student_interfaces__msg__Student__Sequence__copy(
  const student_interfaces__msg__Student__Sequence * input,
  student_interfaces__msg__Student__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(student_interfaces__msg__Student)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(student_interfaces__msg__Student);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    student_interfaces__msg__Student * data =
      (student_interfaces__msg__Student *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!student_interfaces__msg__Student__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          student_interfaces__msg__Student__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!student_interfaces__msg__Student__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
