// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from student_interfaces:srv/Addints.idl
// generated code does not contain a copyright notice

#include "student_interfaces/srv/detail/addints__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_student_interfaces
const rosidl_type_hash_t *
student_interfaces__srv__Addints__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xe5, 0x80, 0xd6, 0x86, 0x57, 0x85, 0xbe, 0xa5,
      0xd9, 0x7d, 0x96, 0x10, 0x7b, 0xd0, 0x73, 0x2b,
      0xe6, 0xc0, 0x34, 0xd8, 0x37, 0x8b, 0xf8, 0x00,
      0x14, 0xa9, 0xbc, 0xfd, 0xfe, 0x01, 0x0f, 0x11,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_student_interfaces
const rosidl_type_hash_t *
student_interfaces__srv__Addints_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x06, 0x84, 0x62, 0x8b, 0xd9, 0x5a, 0x5e, 0x8e,
      0x7e, 0x79, 0xdd, 0xdc, 0xf7, 0x4a, 0x64, 0xa7,
      0xd1, 0xfa, 0x8a, 0x43, 0x83, 0xcd, 0xe1, 0xc2,
      0x32, 0x90, 0xfd, 0xbc, 0x87, 0xc1, 0xb5, 0x20,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_student_interfaces
const rosidl_type_hash_t *
student_interfaces__srv__Addints_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x20, 0xaa, 0xd4, 0x02, 0x74, 0xdf, 0x52, 0x6a,
      0x73, 0x3f, 0xa2, 0x4e, 0x54, 0xcc, 0xc0, 0xb9,
      0x8a, 0x6e, 0x95, 0xda, 0x9f, 0xf0, 0x5f, 0x5f,
      0x6e, 0xb3, 0x54, 0xb4, 0x0b, 0x08, 0x23, 0xc2,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_student_interfaces
const rosidl_type_hash_t *
student_interfaces__srv__Addints_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xd6, 0x4c, 0x3c, 0x3f, 0x48, 0xb7, 0x95, 0xe6,
      0xc2, 0x12, 0x9d, 0xbd, 0xd7, 0x28, 0x20, 0x15,
      0x40, 0xc6, 0x8b, 0xeb, 0x1f, 0x1d, 0xa7, 0x36,
      0x46, 0x50, 0x8b, 0x5c, 0x9e, 0x1a, 0x76, 0x07,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "service_msgs/msg/detail/service_event_info__functions.h"
#include "builtin_interfaces/msg/detail/time__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t service_msgs__msg__ServiceEventInfo__EXPECTED_HASH = {1, {
    0x41, 0xbc, 0xbb, 0xe0, 0x7a, 0x75, 0xc9, 0xb5,
    0x2b, 0xc9, 0x6b, 0xfd, 0x5c, 0x24, 0xd7, 0xf0,
    0xfc, 0x0a, 0x08, 0xc0, 0xcb, 0x79, 0x21, 0xb3,
    0x37, 0x3c, 0x57, 0x32, 0x34, 0x5a, 0x6f, 0x45,
  }};
#endif

static char student_interfaces__srv__Addints__TYPE_NAME[] = "student_interfaces/srv/Addints";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";
static char student_interfaces__srv__Addints_Event__TYPE_NAME[] = "student_interfaces/srv/Addints_Event";
static char student_interfaces__srv__Addints_Request__TYPE_NAME[] = "student_interfaces/srv/Addints_Request";
static char student_interfaces__srv__Addints_Response__TYPE_NAME[] = "student_interfaces/srv/Addints_Response";

// Define type names, field names, and default values
static char student_interfaces__srv__Addints__FIELD_NAME__request_message[] = "request_message";
static char student_interfaces__srv__Addints__FIELD_NAME__response_message[] = "response_message";
static char student_interfaces__srv__Addints__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field student_interfaces__srv__Addints__FIELDS[] = {
  {
    {student_interfaces__srv__Addints__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {student_interfaces__srv__Addints_Request__TYPE_NAME, 38, 38},
    },
    {NULL, 0, 0},
  },
  {
    {student_interfaces__srv__Addints__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {student_interfaces__srv__Addints_Response__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
  {
    {student_interfaces__srv__Addints__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {student_interfaces__srv__Addints_Event__TYPE_NAME, 36, 36},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription student_interfaces__srv__Addints__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {student_interfaces__srv__Addints_Event__TYPE_NAME, 36, 36},
    {NULL, 0, 0},
  },
  {
    {student_interfaces__srv__Addints_Request__TYPE_NAME, 38, 38},
    {NULL, 0, 0},
  },
  {
    {student_interfaces__srv__Addints_Response__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
student_interfaces__srv__Addints__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {student_interfaces__srv__Addints__TYPE_NAME, 30, 30},
      {student_interfaces__srv__Addints__FIELDS, 3, 3},
    },
    {student_interfaces__srv__Addints__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = student_interfaces__srv__Addints_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = student_interfaces__srv__Addints_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[4].fields = student_interfaces__srv__Addints_Response__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char student_interfaces__srv__Addints_Request__FIELD_NAME__num1[] = "num1";
static char student_interfaces__srv__Addints_Request__FIELD_NAME__num2[] = "num2";

static rosidl_runtime_c__type_description__Field student_interfaces__srv__Addints_Request__FIELDS[] = {
  {
    {student_interfaces__srv__Addints_Request__FIELD_NAME__num1, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {student_interfaces__srv__Addints_Request__FIELD_NAME__num2, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
student_interfaces__srv__Addints_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {student_interfaces__srv__Addints_Request__TYPE_NAME, 38, 38},
      {student_interfaces__srv__Addints_Request__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char student_interfaces__srv__Addints_Response__FIELD_NAME__sum[] = "sum";

static rosidl_runtime_c__type_description__Field student_interfaces__srv__Addints_Response__FIELDS[] = {
  {
    {student_interfaces__srv__Addints_Response__FIELD_NAME__sum, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
student_interfaces__srv__Addints_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {student_interfaces__srv__Addints_Response__TYPE_NAME, 39, 39},
      {student_interfaces__srv__Addints_Response__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char student_interfaces__srv__Addints_Event__FIELD_NAME__info[] = "info";
static char student_interfaces__srv__Addints_Event__FIELD_NAME__request[] = "request";
static char student_interfaces__srv__Addints_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field student_interfaces__srv__Addints_Event__FIELDS[] = {
  {
    {student_interfaces__srv__Addints_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {student_interfaces__srv__Addints_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {student_interfaces__srv__Addints_Request__TYPE_NAME, 38, 38},
    },
    {NULL, 0, 0},
  },
  {
    {student_interfaces__srv__Addints_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {student_interfaces__srv__Addints_Response__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription student_interfaces__srv__Addints_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {student_interfaces__srv__Addints_Request__TYPE_NAME, 38, 38},
    {NULL, 0, 0},
  },
  {
    {student_interfaces__srv__Addints_Response__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
student_interfaces__srv__Addints_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {student_interfaces__srv__Addints_Event__TYPE_NAME, 36, 36},
      {student_interfaces__srv__Addints_Event__FIELDS, 3, 3},
    },
    {student_interfaces__srv__Addints_Event__REFERENCED_TYPE_DESCRIPTIONS, 4, 4},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = student_interfaces__srv__Addints_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = student_interfaces__srv__Addints_Response__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "int32 num1\n"
  "int32 num2\n"
  "---\n"
  "int32 sum";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
student_interfaces__srv__Addints__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {student_interfaces__srv__Addints__TYPE_NAME, 30, 30},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 35, 35},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
student_interfaces__srv__Addints_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {student_interfaces__srv__Addints_Request__TYPE_NAME, 38, 38},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
student_interfaces__srv__Addints_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {student_interfaces__srv__Addints_Response__TYPE_NAME, 39, 39},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
student_interfaces__srv__Addints_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {student_interfaces__srv__Addints_Event__TYPE_NAME, 36, 36},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
student_interfaces__srv__Addints__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *student_interfaces__srv__Addints__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[3] = *student_interfaces__srv__Addints_Event__get_individual_type_description_source(NULL);
    sources[4] = *student_interfaces__srv__Addints_Request__get_individual_type_description_source(NULL);
    sources[5] = *student_interfaces__srv__Addints_Response__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
student_interfaces__srv__Addints_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *student_interfaces__srv__Addints_Request__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
student_interfaces__srv__Addints_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *student_interfaces__srv__Addints_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
student_interfaces__srv__Addints_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[5];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 5, 5};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *student_interfaces__srv__Addints_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[3] = *student_interfaces__srv__Addints_Request__get_individual_type_description_source(NULL);
    sources[4] = *student_interfaces__srv__Addints_Response__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
