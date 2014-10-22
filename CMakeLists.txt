cmake_minimum_required (VERSION 2.8.11)
project (saliency_marker)

find_package (Qt5Widgets REQUIRED)

set (CMAKE_AUTOMOC ON)
set (CMAKE_INCLUDE_CURRENT_DIR ON)
set (${PROJECT_NAME}_HEADERS mainwindow.h)
set (${PROJECT_NAME}_SOURCES main.cpp mainwindow.cpp)
qt5_wrap_ui (${PROJECT_NAME}_UIS ui/mainwindow.ui)
qt5_add_resources (${PROJECT_NAME}_QRC images.qrc)

add_executable (${PROJECT_NAME} ${${PROJECT_NAME}_SOURCES}
                                ${${PROJECT_NAME}_HEADERS}
                                ${${PROJECT_NAME}_UIS}
                                ${${PROJECT_NAME}_QRC})
target_link_libraries (${PROJECT_NAME} Qt5::Widgets)
install (TARGETS ${PROJECT_NAME}
         RUNTIME DESTINATION /usr/bin/)
install (FILES images/saliency-marker.png
         DESTINATION /usr/share/icons/hicolor/64x64/apps/)
install (FILES images/saliency-marker.svg
         DESTINATION /usr/share/icons/hicolor/scalable/apps/)
