cmake_minimum_required (VERSION 2.8.11)
project (saliency_marker)

find_package (Qt5Widgets REQUIRED)

set (CMAKE_AUTOMOC ON)
set (CMAKE_INCLUDE_CURRENT_DIR ON)
set (${PROJECT_NAME}_HEADERS mainwindow.h)
set (${PROJECT_NAME}_SOURCES main.cpp mainwindow.cpp)
qt5_wrap_ui (${PROJECT_NAME}_UIS ui/mainwindow.ui)

add_executable (${PROJECT_NAME} ${${PROJECT_NAME}_SOURCES}
                                ${${PROJECT_NAME}_HEADERS}
                                ${${PROJECT_NAME}_UIS})
target_link_libraries (${PROJECT_NAME} Qt5::Widgets)
