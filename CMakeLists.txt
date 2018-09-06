cmake_minimum_required(VERSION 3.5)

project(jaguar4x4)

find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

install(FILES
  resources/teleop_twist_joy_params.yaml
  DESTINATION share/jaguar4x4
)

ament_package()
