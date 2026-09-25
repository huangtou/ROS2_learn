// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from student_interfaces:msg/Student.idl
// generated code does not contain a copyright notice

#include "student_interfaces/msg/detail/student__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_student_interfaces
const rosidl_type_hash_t *
student_interfaces__msg__Student__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x6c, 0xa0, 0xbf, 0xf8, 0xcf, 0x6b, 0xaa, 0x3a,
      0x04, 0x96, 0x93, 0x5e, 0xfa, 0x46, 0xe6, 0x75,
      0xb6, 0x99, 0x32, 0xce, 0x43, 0x46, 0x32, 0xad,
      0xcd, 0x8c, 0x5a, 0xd5, 0x81, 0x2f, 0x5f, 0x21,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char student_interfaces__msg__Student__TYPE_NAME[] = "student_interfaces/msg/Student";

// Define type names, field names, and default values
static char student_interfaces__msg__Student__FIELD_NAME__name[] = "name";
static char student_interfaces__msg__Student__FIELD_NAME__age[] = "age";
static char student_interfaces__msg__Student__FIELD_NAME__height[] = "height";

static rosidl_runtime_c__type_description__Field student_interfaces__msg__Student__FIELDS[] = {
  {
    {student_interfaces__msg__Student__FIELD_NAME__name, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {student_interfaces__msg__Student__FIELD_NAME__age, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {student_interfaces__msg__Student__FIELD_NAME__height, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
student_interfaces__msg__Student__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {student_interfaces__msg__Student__TYPE_NAME, 30, 30},
      {student_interfaces__msg__Student__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "string name\n"
  "int32 age\n"
  "float64 height";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
student_interfaces__msg__Student__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {student_interfaces__msg__Student__TYPE_NAME, 30, 30},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 37, 37},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
student_interfaces__msg__Student__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *student_interfaces__msg__Student__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
